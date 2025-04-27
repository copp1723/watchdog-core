import matplotlib

matplotlib.use('Agg')  # Must be before any other matplotlib imports

# Standard library imports
import os

# init Supabase once
import os as _os
import tempfile
import uuid
from typing import Any, Dict, cast

# Third-party imports
import matplotlib.pyplot as plt
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from pandas import DataFrame
from supabase import create_client

# Local application imports
from api.services.data_cleaner import clean_sales_data
from api.services.metrics import calc_lead_source_roi, calc_rep_leaderboard
from api.services.metrics_sales import (
    cost_per_sale,
    cost_per_sale_by_vendor,
    new_vs_used,
    sales_by_salesperson,
)

_supabase = create_client(
    cast(str, _os.getenv("SUPABASE_URL")), cast(str, _os.getenv("SUPABASE_SERVICE_KEY"))
)

_env = Environment(
    loader=FileSystemLoader("templates/insights"),
    autoescape=True
)

# Helper to upload chart and return public URL
def upload_chart(df: pd.DataFrame) -> str:
    fig, ax = plt.subplots()
    df["net_profit"].plot(kind="barh", ax=ax)
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    fig.savefig(tmp.name)
    plt.close(fig)
    file_name = f"{uuid.uuid4()}.png"
    _supabase.storage.from_("charts").upload(file_name, open(tmp.name, "rb"))
    url = (
        _supabase.storage.from_("charts")
        .get_public_url(file_name)
        .replace(" ", "%20")
    )
    os.remove(tmp.name)
    return cast(str, url)

def generate(
    insight_request: Dict[str, Any], 
    dataframe: pd.DataFrame
) -> Dict[str, Any]:
    intent = insight_request.get("intent")

    registry = {
        "lead_source_roi": calc_lead_source_roi,
        "rep_leaderboard": calc_rep_leaderboard,
        "cost_per_sale": cost_per_sale,
        "cost_per_sale_by_vendor": cost_per_sale_by_vendor,
        "sales_by_salesperson": sales_by_salesperson,
        "new_vs_used": new_vs_used,
    }

    if intent not in registry:
        raise ValueError(f"Unknown intent '{intent}'")

    df_clean = clean_sales_data(dataframe)
    data = registry[intent](df_clean)

    if intent == "lead_source_roi":
        df_result = pd.DataFrame(cast(list[dict[str, Any]], data))
        top = df_result.iloc[0]
        lag = df_result.iloc[-1]
        headline = {
            "top_source": top["lead_source"],
            "top_net": int(top["net_profit"]),
            "top_speed": int(top["avg_days"]),
            "lagging_source": lag["lead_source"],
            "shift_budget": 1000,  # Example static value
            "roi_delta": (
                (top["net_profit"] - lag["net_profit"]) / lag["net_profit"] 
                if lag["net_profit"] else 0
            ),
        }
        chart_url = upload_chart(df_result)
        template = _env.get_template(f"{intent}.j2")
        html = template.render(**headline)
        return {
            "title": intent,
            "html": html,
            "chart_url": chart_url,
            "data": df_result.to_dict(),
        }
    elif intent in ["cost_per_sale_by_vendor", "sales_by_salesperson", "new_vs_used"]:
        data_dict = cast(dict[str, Any], data)
        headline = data_dict["headline"]
        template = _env.get_template(f"{intent}.j2")
        html = template.render(**headline)
        return {
            "title": intent,
            "html": html,
            "data": data,
        }
    else:
        # Fallback for other metrics
        return {
            "title": intent,
            "data": data,
        }

def generate_legacy(intent: dict[str, Any], df: DataFrame) -> dict[str, Any]:
    df = clean_sales_data(df)
    metric = intent["metric"]
    agg = intent["aggregation"]  # "sum" | "mean" | "count"
    group_by = intent.get("category")

    if metric not in df.columns:
        raise ValueError(f"Unknown metric {metric}")

    if group_by:
        grouped = df.groupby(group_by)[metric]
        value = getattr(grouped, agg)()
        # simple bar chart
        fig, ax = plt.subplots()
        value.plot(kind="bar", ax=ax)
    else:
        value = getattr(df[metric], agg)()
        # pie chart with single slice placeholder
        fig, ax = plt.subplots()
        ax.bar(["total"], [value])

    ax.set_title(f"{agg}({metric})")
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    fig.savefig(tmp.name)
    plt.close(fig)

    # upload to Supabase bucket "charts"
    file_name = f"{uuid.uuid4()}.png"
    _supabase.storage.from_("charts").upload(file_name, open(tmp.name, "rb"))
    url = (
        _supabase.storage.from_("charts")
        .get_public_url(file_name)
        .replace(" ", "%20")
    )

    os.remove(tmp.name)
    return {
        "metric": metric,
        "aggregation": agg,
        "value": float(value) if not hasattr(value, "to_dict") else cast(Any, value).to_dict(),
        "chart_url": url,
    } 
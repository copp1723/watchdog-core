from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import tempfile, os
from supabase import create_client
import uuid, datetime
from api.services.data_cleaner import clean_sales_data

# init Supabase once
import os as _os
_supabase = create_client(
    _os.getenv("SUPABASE_URL"), _os.getenv("SUPABASE_SERVICE_KEY")
)

def generate(intent: dict, df: DataFrame) -> dict:
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
        "value": float(value) if not hasattr(value, "to_dict") else value.to_dict(),
        "chart_url": url,
    } 
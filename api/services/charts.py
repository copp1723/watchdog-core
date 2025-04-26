import matplotlib.pyplot as plt
import tempfile, os
from supabase import create_client
import uuid
import os as _os
import pandas as pd

_supabase = create_client(
    _os.getenv("SUPABASE_URL"), _os.getenv("SUPABASE_SERVICE_KEY")
)

CHART_STYLES = {
    'font.family': 'DejaVu Sans',
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'axes.edgecolor': '#333333',
    'axes.linewidth': 1.2,
}
plt.rcParams.update(CHART_STYLES)

BAR_COLOR = '#2A7FFF'
STACKED_COLORS = ['#2A7FFF', '#FFB32A']


def generate_chart(data: pd.DataFrame, chart_type: str, title: str = "", xlabel: str = "", ylabel: str = "") -> str:
    fig, ax = plt.subplots(figsize=(7, 4))
    if chart_type == "horizontal_bar":
        data.plot(kind="barh", color=BAR_COLOR, ax=ax, legend=False)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
    elif chart_type == "vertical_bar":
        data.plot(kind="bar", color=BAR_COLOR, ax=ax, legend=False)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
    elif chart_type == "stacked_bar":
        data.plot(kind="bar", stacked=True, color=STACKED_COLORS, ax=ax)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
    else:
        raise ValueError(f"Unknown chart_type: {chart_type}")
    ax.set_title(title)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
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
    return url 
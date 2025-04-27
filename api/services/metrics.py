from typing import Any, cast
import pandas as pd


def calc_lead_source_roi(df: pd.DataFrame) -> list[dict[str, Any]]:
    roi = df.groupby('lead_source').agg(
        net_profit=('net_profit', 'sum'),
        avg_days=('days_to_close', 'mean')
    ).sort_values('net_profit', ascending=False).reset_index()
    return cast(list[dict[str, Any]], roi.to_dict(orient='records'))

def calc_rep_leaderboard(df: pd.DataFrame) -> list[dict[str, Any]]:
    leaderboard = df.groupby('sales_rep_name').agg(
        net_profit=('net_profit', 'sum'),
        avg_margin_pct=('margin_pct', 'mean')
    ).sort_values('net_profit', ascending=False).reset_index()
    return cast(list[dict[str, Any]], leaderboard.to_dict(orient='records')) 
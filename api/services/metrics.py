import pandas as pd
from typing import Dict, Any

def calc_lead_source_roi(df: pd.DataFrame) -> Dict[str, Any]:
    roi = df.groupby('lead_source').agg(
        net_profit=('net_profit', 'sum'),
        avg_days=('days_to_close', 'mean')
    ).sort_values('net_profit', ascending=False).reset_index()
    return roi.to_dict(orient='records')

def calc_rep_leaderboard(df: pd.DataFrame) -> Dict[str, Any]:
    leaderboard = df.groupby('sales_rep_name').agg(
        net_profit=('net_profit', 'sum'),
        avg_margin_pct=('margin_pct', 'mean')
    ).sort_values('net_profit', ascending=False).reset_index()
    return leaderboard.to_dict(orient='records') 
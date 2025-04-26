import pandas as pd
from typing import Dict, Any

def cost_per_sale(df: pd.DataFrame) -> float:
    return df['expense'].sum() / len(df)

def cost_per_sale_by_vendor(df: pd.DataFrame) -> Dict[str, float]:
    return df.groupby('lead_source')['expense'].mean().to_dict()

def sales_by_salesperson(df: pd.DataFrame) -> Dict[str, int]:
    return df['sales_rep_name'].value_counts().to_dict()

def new_vs_used(df: pd.DataFrame) -> Dict[str, int]:
    return df['is_new'].value_counts().to_dict() 
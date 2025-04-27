from typing import Any

import pandas as pd


def cost_per_sale(df: pd.DataFrame) -> float:
    return float(df['expense'].sum()) / len(df)

def cost_per_sale_by_vendor(df: pd.DataFrame) -> dict[str, float | str | dict[str, float | str]]:
    cps = df.groupby('lead_source')['expense'].mean().to_dict()
    if not cps:
        return {}
    worst_vendor = max(cps, key=lambda k: cps[k])
    best_vendor = min(cps, key=lambda k: cps[k])
    worst_cps = cps[worst_vendor]
    best_cps = cps[best_vendor]
    shift_pct = 0.1  # Example static value
    return {
        'worst_vendor': worst_vendor,
        'worst_cps': worst_cps,
        'best_vendor': best_vendor,
        'best_cps': best_cps,
        'shift_pct': shift_pct,
        'headline': {
            'worst_vendor': worst_vendor,
            'worst_cps': worst_cps,
            'best_vendor': best_vendor,
            'best_cps': best_cps,
            'shift_pct': shift_pct,
        }
    }

def sales_by_salesperson(df: pd.DataFrame) -> dict[str, float | str | dict[str, float | str]]:
    sales = df['sales_rep_name'].value_counts().to_dict()
    if not sales:
        return {}
    top_rep = max(sales, key=lambda k: sales[k])
    low_rep = min(sales, key=lambda k: sales[k])
    top_sales = sales[top_rep]
    low_sales = sales[low_rep]
    return {
        'top_rep': top_rep,
        'top_sales': top_sales,
        'low_rep': low_rep,
        'low_sales': low_sales,
        'headline': {
            'top_rep': top_rep,
            'top_sales': top_sales,
            'low_rep': low_rep,
            'low_sales': low_sales,
        }
    }

def new_vs_used(df: pd.DataFrame) -> dict[str, float | str | dict[str, float | str]]:
    counts = df['is_new'].value_counts().to_dict()
    new_count = counts.get(True, 0)
    used_count = counts.get(False, 0)
    return {
        'new_count': new_count,
        'used_count': used_count,
        'headline': {
            'new_count': new_count,
            'used_count': used_count,
        }
    } 
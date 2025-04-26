"""
Column mapping service for handling different CSV formats and field naming conventions.

This module provides functionality to normalize column names from various dealer CSV exports
to a standard canonical format, allowing the application to work with different data formats
without requiring manual intervention.
"""

from typing import Dict, List, Set
import pandas as pd

# Dictionary mapping canonical field names to all possible aliases that might be found in CSV files
ALIAS_MAP: Dict[str, List[str]] = {
    "sold_date":  ["sold_date", "date_sold", "sale_date"],
    "vehicle":    ["vehicle", "model", "vehicle_desc"],
    "sold_price": ["sold_price", "sale_price", "selling_price"],
    "listing_price": ["listing_price", "ask_price", "sticker"],
    "profit":     ["profit", "front_gross"],
    "gross":      ["gross", "front_gross"],   # canonical = gross
    "expense":    ["expense", "lead_cost", "marketing_spend"],
    "lead_source": ["lead_source", "vendor", "source"],
    "sales_rep_name": ["sales_rep_name", "rep", "salesperson"],
    "is_new":     ["is_new", "new_used_flag"],
    "days_to_close": ["days_to_close", "lead_age"],
}

def normalise_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform DataFrame columns to use canonical names based on the ALIAS_MAP.
    
    Args:
        df: pandas DataFrame with original column names from CSV
        
    Returns:
        DataFrame with standardized column names
        
    Raises:
        ValueError: If required columns are missing after mapping
    """
    rename_map = {}
    for canon, aliases in ALIAS_MAP.items():
        for a in aliases:
            if a in df.columns:
                rename_map[a] = canon
                break
    
    # Apply the renaming
    df = df.rename(columns=rename_map)

    # Check for required columns
    missing = [c for c in ["sold_date", "vehicle", "sold_price"] if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns after mapping: {missing}")
    
    return df


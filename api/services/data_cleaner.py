import pandas as pd
from typing import List
from .column_map import normalise_columns

def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and prepare sales data by normalizing column names and deriving additional fields.
    
    Args:
        df: Raw pandas DataFrame from CSV import
        
    Returns:
        Cleaned DataFrame with standardized column names and derived fields
    """
    # First, normalize all column names to canonical format
    df = normalise_columns(df)
    
    # Derive missing but computable fields
    if 'profit' in df.columns and 'cost' not in df.columns and 'sold_price' in df.columns:
        df['cost'] = df['sold_price'] - df['profit']
    
    # Ensure gross is available (canonical name for profit)
    if 'profit' in df.columns and 'gross' not in df.columns:
        df['gross'] = df['profit']
    
    # Clean numeric columns if they exist
    numeric_cols: List[str] = ['listing_price', 'sold_price', 'profit', 'expense', 'cost', 'gross']
    for col in numeric_cols:
        if col in df.columns:
            # Handle string values with $ or commas
            if df[col].dtype == object:
                df[col] = df[col].replace(r'[$,]', '', regex=True).astype(float)
            # Ensure numeric type
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Calculate derived columns only if required columns exist
    if 'listing_price' in df.columns and 'sold_price' in df.columns:
        df['discount'] = df['listing_price'] - df['sold_price']
    
    if 'profit' in df.columns and 'sold_price' in df.columns:
        df['margin_pct'] = df['profit'] / df['sold_price']
    
    if 'profit' in df.columns and 'expense' in df.columns:
        df['net_profit'] = df['profit'] - df['expense']
    elif 'profit' in df.columns and 'cost' in df.columns:
        # Alternative calculation using cost if expense isn't available
        df['net_profit'] = df['profit'] - df['cost']
    
    return df

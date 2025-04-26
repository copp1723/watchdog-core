import pandas as pd

def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    for col in ['listing_price', 'sold_price', 'profit', 'expense']:
        df[col] = df[col].replace('[\$,]', '', regex=True).astype(float)
    df['discount'] = df['listing_price'] - df['sold_price']
    df['margin_pct'] = df['profit'] / df['sold_price']
    df['net_profit'] = df['profit'] - df['expense']
    return df 
import pandas as pd
from api.services.data_cleaner import clean_sales_data
import pathlib

SAMPLE = pathlib.Path("tests") / "sample_sales.csv"
df_raw = pd.read_csv(SAMPLE)
df = clean_sales_data(df_raw) 
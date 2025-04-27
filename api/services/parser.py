import pandas as pd
from api.models.sales_log import SalesLogRow, ValidationError

def validate_csv(path: str) -> list[SalesLogRow]:
    df = pd.read_csv(path)
    
    # Filter dataframe to only include columns defined in SalesLogRow
    valid_columns = [col for col in SalesLogRow.model_fields.keys() if col in df.columns]
    df = df[valid_columns]
    
    try:
        return [SalesLogRow(**row.to_dict()) for _, row in df.iterrows()]
    except ValidationError as e:
        raise ValueError(e.errors()) 

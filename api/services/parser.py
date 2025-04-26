import pandas as pd
from api.models.sales_log import SalesLogRow, ValidationError

def validate_csv(path: str) -> list[SalesLogRow]:
    df = pd.read_csv(path)
    try:
        return [SalesLogRow(**row.to_dict()) for _, row in df.iterrows()]
    except ValidationError as e:
        raise ValueError(e.errors()) 
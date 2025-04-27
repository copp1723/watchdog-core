import pandas as pd
from api.models.sales_log import SalesLogRow, ValidationError

def validate_csv(path: str) -> list[SalesLogRow]:
    df = pd.read_csv(path)
    
    # Build set of valid column names: canonical names and aliases
    valid_columns = set()
    for name, field in SalesLogRow.model_fields.items():
        valid_columns.add(name)
        if field.alias:
            valid_columns.add(field.alias)

    # Filter dataframe to only include columns defined in SalesLogRow (by name or alias)
    filtered_columns = [col for col in df.columns if col in valid_columns]
    df = df[filtered_columns]
    
    try:
        return [SalesLogRow(**row.to_dict()) for _, row in df.iterrows()]
    except ValidationError as e:
        raise ValueError(e.errors()) 

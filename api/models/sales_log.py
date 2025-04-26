from pydantic import BaseModel, Field, ValidationError
from datetime import date

class SalesLogRow(BaseModel):
    sold_date: date = Field(..., alias="sold_date")
    vehicle: str
    sold_price: float
    cost: float
    profit: float
    gross: float
    lead_source: str | None = None
    salesperson: str | None = None

    model_config = {
        "extra": "forbid",   # reject unknown columns
        "populate_by_name": True,
    } 
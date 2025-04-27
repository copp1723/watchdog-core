from pydantic import BaseModel, Field, ValidationError
from datetime import date
from typing import Optional

class SalesLogRow(BaseModel):
    """
    Model for a row in the sales log data.
    
    Contains required core fields and optional derived fields.
    All fields use canonical names that are standardized through the column mapper.
    """
    # Core required fields
    sold_date: date = Field(..., description="Date when the vehicle was sold")
    vehicle: str = Field(..., description="Vehicle description or model")
    sold_price: float = Field(..., description="Final price the vehicle was sold for")
    
    # Optional fields that might be derived
    cost: Optional[float] = Field(None, description="Dealer's cost for the vehicle")
    gross: Optional[float] = Field(None, description="Gross profit from the sale")
    profit: Optional[float] = Field(None, description="Profit from the sale (may be same as gross)")
    listing_price: Optional[float] = Field(None, description="Original asking price")
    expense: Optional[float] = Field(None, description="Marketing or lead acquisition cost")
    discount: Optional[float] = Field(None, description="Difference between listing and sold price")
    days_to_close: Optional[int] = Field(None, description="Number of days from lead to sale")
    
    # Categorical fields
    lead_source: Optional[str] = Field(None, description="Source of the lead (marketing channel)")
    sales_rep_name: Optional[str] = Field(None, description="Name of the sales representative", alias="salesperson")
    is_new: Optional[bool] = Field(None, description="Whether the vehicle was new or used")
    
    # Derived financial metrics
    margin_pct: Optional[float] = Field(None, description="Profit as percentage of sale price")
    net_profit: Optional[float] = Field(None, description="Profit minus expenses")

    model_config = {
        "extra": "forbid",   # reject unknown columns
        "populate_by_name": True,
    }

import os
import pandas as pd
from fastapi import APIRouter, HTTPException
from tempfile import gettempdir
from api.services.insight_engine import generate, generate_legacy
from api.services.parser import validate_csv
from typing import Any

router = APIRouter(prefix="/v1", tags=["analyze"])

@router.post("/analyze/{upload_id}")
async def analyze(upload_id: str, query: dict[str, Any]) -> dict[str, Any]:
    path = os.path.join(gettempdir(), f"{upload_id}.csv")
    if not os.path.exists(path):
        raise HTTPException(404, "upload_id not found")

    rows = validate_csv(path)
    df = pd.DataFrame([r.model_dump() for r in rows])

    # Check if this is a legacy query format with metric and aggregation
    if "metric" in query and "aggregation" in query:
        insight = generate_legacy(query, df)
    else:
        # New format with intent
        insight = generate(query, df)
    return insight 

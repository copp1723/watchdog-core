import os

import pandas as pd
from fastapi import APIRouter, HTTPException

from api.routes.upload import tempfile
from api.services.insight_engine import generate, generate_legacy
from api.services.parser import validate_csv

router = APIRouter(prefix="/v1", tags=["analyze"])

@router.post("/analyze/{upload_id}")
async def analyze(upload_id: str, query: dict):
    path = os.path.join(tempfile.gettempdir(), f"{upload_id}.csv")
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

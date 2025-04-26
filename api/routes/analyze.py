from fastapi import APIRouter, HTTPException
from api.services.insight_engine import generate
from api.services.parser import validate_csv
from api.routes.upload import tempfile
import os, json

router = APIRouter(prefix="/v1", tags=["analyze"])

@router.post("/analyze/{upload_id}")
async def analyze(upload_id: str, query: dict):
    path = os.path.join(tempfile.gettempdir(), f"{upload_id}.csv")
    if not os.path.exists(path):
        raise HTTPException(404, "upload_id not found")

    rows = validate_csv(path)
    import pandas as pd

    df = pd.DataFrame([r.model_dump() for r in rows])

    # TEMP: ask LLM later; for now accept query body as intent
    insight = generate(query, df)
    return insight 
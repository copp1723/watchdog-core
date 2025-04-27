import os
import shutil
import tempfile
import uuid

from fastapi import APIRouter, File, HTTPException, UploadFile

from api.services.parser import validate_csv

router = APIRouter(prefix="/v1", tags=["upload"])

@router.post("/upload")
async def upload_csv(file: UploadFile = None):
    file = file or File(...)
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only .csv files accepted")

    upload_id = str(uuid.uuid4())
    tmp_path = os.path.join(tempfile.gettempdir(), f"{upload_id}.csv")

    with open(tmp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        rows = validate_csv(tmp_path)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    return {
        "upload_id": upload_id,
        "rows": len(rows)
    } 
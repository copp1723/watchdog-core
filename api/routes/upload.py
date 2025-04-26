from fastapi import APIRouter, UploadFile, File, HTTPException
import uuid, shutil, os, tempfile

router = APIRouter(prefix="/v1", tags=["upload"])

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only .csv files accepted")

    upload_id = str(uuid.uuid4())
    tmp_path = os.path.join(tempfile.gettempdir(), f"{upload_id}.csv")

    with open(tmp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"upload_id": upload_id} 
from fastapi import APIRouter, HTTPException
router = APIRouter(prefix="/debug")

@router.get("/boom")
async def boom():
    raise HTTPException(status_code=500, detail="crash test") 
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/debug")

@router.get("/boom", response_model=None)
async def boom() -> None:
    raise HTTPException(status_code=500, detail="crash test") 
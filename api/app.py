"""
Main FastAPI application for Watchdog Core.
"""
from fastapi import FastAPI
from api.routes import upload  # <-- import

app = FastAPI(title="Watchdog Core API")
app.include_router(upload.router)  # <-- mount


@app.get("/healthz")
async def health_check() -> dict[str, str]:
    """
    Health check endpoint.
    
    Returns:
        A status response indicating the API is operational.
    """
    return {"status": "ok"}


"""
Main FastAPI application for Watchdog Core.
"""
from fastapi import FastAPI

app = FastAPI(title="Watchdog Core API")


@app.get("/healthz")
async def health_check() -> dict[str, str]:
    """
    Health check endpoint.
    
    Returns:
        A status response indicating the API is operational.
    """
    return {"status": "ok"}


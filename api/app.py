"""
Main FastAPI application for Watchdog Core.
"""
import os, sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from fastapi import FastAPI
from api.routes import upload  # <-- import
from api.routes import debug

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN", ""),
    traces_sample_rate=0.1,  # 10 % for now
)

app = FastAPI(title="Watchdog Core API")
app.add_middleware(SentryAsgiMiddleware)
app.include_router(upload.router)  # <-- mount
app.include_router(debug.router)


@app.get("/healthz")
async def health_check() -> dict[str, str]:
    """
    Health check endpoint.
    
    Returns:
        A status response indicating the API is operational.
    """
    return {"status": "ok"}


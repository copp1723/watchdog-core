"""
Main FastAPI application for Watchdog Core.
"""
import os
import sentry_sdk
from fastapi import FastAPI
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from api.otel import instrument_fastapi
from api.routes import analyze
from api.routes import debug
from api.routes import upload  # <-- import

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN", ""),
    traces_sample_rate=0.1,  # 10 % for now
)

app = FastAPI(title="Watchdog Core API")
app.add_middleware(SentryAsgiMiddleware)
instrument_fastapi(app)
app.include_router(upload.router)  # <-- mount
app.include_router(debug.router)
app.include_router(analyze.router)


@app.get("/healthz")
async def health_check() -> dict[str, str]:
    """
    Health check endpoint.
    
    Returns:
        A status response indicating the API is operational.
    """
    return {"status": "ok"}


@app.get("/metrics")
async def metrics():
    return {"status": "metrics stub"}


"""
Main FastAPI application for Watchdog Core.
"""
import os
from typing import Any

import sentry_sdk
from fastapi import FastAPI
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from api.otel import instrument_fastapi
from api.routes import (
    analyze,
    debug,
    upload,  # <-- import
)

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN", ""),
    traces_sample_rate=0.1,  # 10 % for now
)

app = FastAPI(title="Watchdog Core API")
app.add_middleware(SentryAsgiMiddleware)  # type: ignore[arg-type]
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
async def metrics() -> dict[str, str]:
    return {"status": "metrics stub"}


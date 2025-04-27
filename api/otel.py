import logging
import os
from typing import Optional, Any

# Initialize logger
logger = logging.getLogger(__name__)

# Flag to track if OpenTelemetry is enabled
otel_enabled = False

# Initialize variables to None
provider = None
exporter = None

def is_otel_enabled() -> bool:
    """
    Check if OpenTelemetry is enabled.
    
    Returns:
        bool: True if OpenTelemetry is enabled, False otherwise.
    """
    return otel_enabled

def setup_opentelemetry() -> bool:
    """
    Set up OpenTelemetry if configured.
    
    Returns:
        bool: True if setup was successful, False otherwise.
    """
    global provider, exporter, otel_enabled
    
    # Check if OpenTelemetry endpoint is configured
    endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "")
    
    # If endpoint is empty, don't initialize OpenTelemetry
    if not endpoint:
        logger.info("OpenTelemetry endpoint not configured, tracing disabled")
        return False

    try:
        # Import OpenTelemetry modules only if we're going to use them
        from opentelemetry import trace
        from opentelemetry.exporter.otlp.proto.http.trace_exporter import (
            OTLPSpanExporter,
        )
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import BatchSpanProcessor
        
        # Initialize provider
        provider = TracerProvider()
        trace.set_tracer_provider(provider)
        
        # Initialize exporter with error handling
        try:
            exporter = OTLPSpanExporter(endpoint=endpoint)
            provider.add_span_processor(BatchSpanProcessor(exporter))
            otel_enabled = True
            logger.info(f"OpenTelemetry initialized with endpoint: {endpoint}")
            return True
        except Exception as e:
            logger.warning(f"Failed to initialize OpenTelemetry exporter: {str(e)}")
            return False
    except ImportError as e:
        logger.warning(f"OpenTelemetry packages not available: {str(e)}")
        return False
    except Exception as e:
        logger.warning(f"Unexpected error setting up OpenTelemetry: {str(e)}")
        return False

# Initialize OpenTelemetry if configured
setup_opentelemetry()

# Import instrumentation modules
_fastapi_instrumentor: Optional[Any]
try:
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
    _fastapi_instrumentor = FastAPIInstrumentor
except ImportError:
    logger.warning("FastAPI instrumentation not available")
    _fastapi_instrumentor = None

def instrument_fastapi(app: Any) -> None:
    """
    Instrument a FastAPI application with OpenTelemetry.
    
    Args:
        app: The FastAPI application to instrument.
    """
    if not is_otel_enabled() or _fastapi_instrumentor is None:
        logger.info("Skipping FastAPI instrumentation as OpenTelemetry is disabled")
        return
    
    try:
        _fastapi_instrumentor.instrument_app(app)
        logger.info("FastAPI application instrumented with OpenTelemetry")
    except Exception as e:
        logger.warning(f"Failed to instrument FastAPI application: {str(e)}")

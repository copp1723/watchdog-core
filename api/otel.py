from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
import os

provider = TracerProvider()
trace.set_tracer_provider(provider)

endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4318")
exporter = OTLPSpanExporter(endpoint=endpoint)
provider.add_span_processor(BatchSpanProcessor(exporter))

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

# call this after FastAPI app is created
def instrument_fastapi(app):
    FastAPIInstrumentor.instrument_app(app) 
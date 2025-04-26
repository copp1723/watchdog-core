"""
Tests for the health check endpoint.
"""
from fastapi.testclient import TestClient

from api.app import app


def test_health_check():
    """Test that the health check endpoint returns the expected response."""
    client = TestClient(app)
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


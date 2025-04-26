import pytest
from fastapi.testclient import TestClient
from api.app import app

def test_metrics():
    client = TestClient(app)
    response = client.get("/metrics")
    assert response.status_code == 200
    assert response.json() == {"status": "metrics stub"} 
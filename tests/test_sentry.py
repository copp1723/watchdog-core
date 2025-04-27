from fastapi.testclient import TestClient
from api.app import app
client = TestClient(app)

def test_boom() -> None:
    resp = client.get("/debug/boom")
    assert resp.status_code == 500 
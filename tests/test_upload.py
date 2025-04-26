from fastapi.testclient import TestClient
from api.app import app
import io

client = TestClient(app)

def test_upload_returns_id():
    csv_bytes = b"sold_date,vehicle,sold_price,cost,profit,gross\n2024-01-01,Toyota,20000,15000,5000,5000\n"
    resp = client.post(
        "/v1/upload",
        files={"file": ("sample.csv", io.BytesIO(csv_bytes), "text/csv")},
    )
    assert resp.status_code == 200
    assert "upload_id" in resp.json()
    assert resp.json()["rows"] == 1

def test_upload_bad_csv():
    bad = b"nope,bad\n1,2\n"
    resp = client.post(
        "/v1/upload",
        files={"file": ("bad.csv", bad, "text/csv")},
    )
    assert resp.status_code == 400 
from api.app import app
from fastapi.testclient import TestClient
import io

client = TestClient(app)

def test_sum_insight():
    csv = b"sold_date,vehicle,sold_price,cost,profit,gross\n2025-04-01,F150,30000,25000,5000,4500"
    res = client.post("/v1/upload", files={"file": ("s.csv", io.BytesIO(csv), "text/csv")})
    uid = res.json()["upload_id"]

    intent = {"metric": "sold_price", "aggregation": "sum"}
    out = client.post(f"/v1/analyze/{uid}", json=intent)
    assert out.status_code == 200
    body = out.json()
    assert body["value"] == 30000
    assert body["chart_url"].startswith("http") 
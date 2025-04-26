from fastapi.testclient import TestClient
from api.app import app
import io

client = TestClient(app)

def test_upload_returns_id():
    csv_bytes = b"col1,col2\n1,2\n"
    resp = client.post(
        "/v1/upload",
        files={"file": ("sample.csv", io.BytesIO(csv_bytes), "text/csv")},
    )
    assert resp.status_code == 200
    assert "upload_id" in resp.json() 
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
TOKEN = "Bearer secret-token"

def test_ingest_and_summary():
    tx = [{
        "user_id": "user_456",
        "amount": 1500.00,
        "category": "Groceries",
        "narration": "Test",
        "timestamp": "2024-12-15T12:00:00Z"
    }]
    
    resp = client.post("/ingest", json=tx, headers={"Authorization": TOKEN})
    assert resp.status_code == 200

    resp2 = client.get("/summary?user_id=user_456&month=2024-12", headers={"Authorization": TOKEN})
    assert resp2.status_code == 200
    assert resp2.json()["user_id"] == "user_456"

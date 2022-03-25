from fastapi.testclient import TestClient
from prog import app

client = TestClient(app, base_url="http://localhost:8100")


def test_get():
    user_id = "abcde"
    res = client.get(f"/v1/user/{user_id}")
    assert res.status_code == 200
    assert res.json()["user_name"] == f"{user_id} 一郎さん"
    assert res.json()["age"] == 12

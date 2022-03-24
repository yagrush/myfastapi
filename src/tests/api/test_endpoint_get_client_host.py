from fastapi.testclient import TestClient
from prog import app
from routers.api.getClientHost.endpoint import API_NAME

client = TestClient(app)


def test_endpoint_get_client_host():
    res = client.get(f"/{API_NAME}")
    assert res.status_code == 200
    assert res.json()["result"] == "testclient"

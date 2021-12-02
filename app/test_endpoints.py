from .main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_home():
    res = client.get("/")
    assert res.status_code == 200
    assert res.headers['content-type'] == "application/json"
    assert res.json()== "hello"
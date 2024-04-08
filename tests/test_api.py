# test_main.py
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_item():
    response = client.get("/items/5?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "q": "test"}

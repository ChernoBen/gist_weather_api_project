from fastapi.testclient import TestClient
from src.app import app 

client = TestClient(app)

# Testing if root endpoint return a response 200
def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Weather API!"}
from fastapi.testclient import TestClient
from src.app import app 

client = TestClient(app)

# Testing if root endpoint returns a response 200
def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Weather API!"}
    
# Testing if swagger endpoint returns a response 200    
def test_swagger_ui_accessible():
    response = client.get("/docs")
    assert response.status_code == 200
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from src.controllers.gist_controller import router
from fastapi import HTTPException


client = TestClient(router)

# Testing if an url is returned when a valid input was passed
@patch('src.controllers.gist_controller.GistService')
def test_create_gist_success(mock_gist_service):
    mock_gist_instance = mock_gist_service.return_value
    mock_gist_instance.create_new_gist.return_value = "http://gist.url"
    
    response = client.post("/gist/", json={"city": "Itajai", "country": "br"})

    assert response.status_code == 200
    assert response.json() == {"url": "http://gist.url"}
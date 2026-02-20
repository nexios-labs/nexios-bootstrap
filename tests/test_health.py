import pytest
from nexios.testclient import TestClient
from src.main import app


def test_get_health_check():
    """Test GET /health/ endpoint"""
    client = TestClient(app)
    response = client.get("/health/")
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["status"] == "ok"
    assert "service" in data
    assert "timestamp" in data
    assert "version" in data
    assert data["service"] == "nexios-starter"


def test_post_health_check():
    """Test POST /health/ endpoint"""
    client = TestClient(app)
    payload = {
        "service_name": "test-service",
        "include_details": True,
        "start_number": 1,
        "end_number": 3
    }
    
    response = client.post("/health/", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["status"] == "ok"
    assert data["service"] == "test-service"
    assert "counting_result" in data
    
    counting = data["counting_result"]
    assert counting["numbers"] == [1, 2, 3]
    assert counting["total_count"] == 3


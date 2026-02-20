import pytest
import asyncio
from nexios.testclient import TestClient
from src.main import app


class TestHealthCheck:
    """Test health check endpoints"""
    
    def setup_method(self):
        """Setup test client"""
        self.client = TestClient(app)
    
    def test_get_health_check(self):
        """Test GET /health/ endpoint"""
        response = self.client.get("/health/")
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["status"] == "ok"
        assert "service" in data
        assert "timestamp" in data
        assert "version" in data
        assert data["service"] == "nexios-starter"
    
    def test_post_health_check_basic(self):
        """Test POST /health/ endpoint with basic request"""
        response = self.client.post("/health/", json={})
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["status"] == "ok"
        assert "service" in data
        assert "timestamp" in data
        assert "version" in data
    
    def test_post_health_check_with_details(self):
        """Test POST /health/ endpoint with details enabled"""
        payload = {
            "service_name": "test-service",
            "check_type": "comprehensive",
            "include_details": True,
            "start_number": 1,
            "end_number": 5,
            "step": 1
        }
        
        response = self.client.post("/health/", json=payload)
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["status"] == "ok"
        assert data["service"] == "test-service"
        assert "counting_result" in data
        
        counting = data["counting_result"]
        assert counting["start"] == 1
        assert counting["end"] == 5
        assert counting["step"] == 1
        assert counting["total_count"] == 5
        assert counting["numbers"] == [1, 2, 3, 4, 5]
    
    def test_post_health_check_with_custom_counting(self):
        """Test POST /health/ endpoint with custom counting parameters"""
        payload = {
            "start_number": 10,
            "end_number": 15,
            "step": 2,
            "include_details": True
        }
        
        response = self.client.post("/health/", json=payload)
        
        assert response.status_code == 200
        data = response.json()
        
        assert "counting_result" in data
        counting = data["counting_result"]
        assert counting["numbers"] == [10, 12, 14]
        assert counting["total_count"] == 3
    
    def test_post_health_check_invalid_json(self):
        """Test POST /health/ endpoint with invalid JSON"""
        response = self.client.post(
            "/health/",
            data="invalid json",
            headers={"Content-Type": "application/json"}
        )
        
        assert response.status_code == 400
    
    def test_health_check_cors_headers(self):
        """Test CORS headers are present"""
        response = self.client.get("/health/")
        
        assert response.status_code == 200
        # CORS headers should be added by middleware
        assert "access-control-allow-origin" in response.headers or "Access-Control-Allow-Origin" in response.headers
    
    def test_health_check_response_headers(self):
        """Test custom response headers"""
        response = self.client.get("/health/")
        
        assert response.status_code == 200
        assert "x-service-status" in response.headers or "X-Service-Status" in response.headers
        assert "cache-control" in response.headers or "Cache-Control" in response.headers


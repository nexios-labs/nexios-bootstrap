import pytest
import os
import sys
from pathlib import Path

# Add src to path for testing
sys.path.insert(0, str(Path(__file__).parent.parent))

from nexios.testclient import TestClient
from src.main import app


@pytest.fixture
def client():
    """Test client fixture"""
    return TestClient(app)


@pytest.fixture
async def async_client():
    """Async test client fixture"""
    from nexios.testclient import AsyncTestClient

    async with AsyncTestClient(app) as client:
        yield client


@pytest.fixture
def mock_env():
    """Mock environment variables for testing"""
    original_env = os.environ.copy()

    # Set test environment
    os.environ.update(
        {
            "APP_ENV": "testing",
            "DEBUG": "true",
            "LOG_LEVEL": "ERROR",  # Reduce log noise in tests
        }
    )

    yield

    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)

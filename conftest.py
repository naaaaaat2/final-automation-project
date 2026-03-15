import pytest
from api.client import APIClient
from config.settings import Config

# Проверяем конфигурацию
Config.validate()

@pytest.fixture(scope="function")
def api_client():
    """Fixture for API client without auth"""
    return APIClient()

@pytest.fixture(scope="function")
def auth_api_client():
    """Fixture for API client with API key"""
    if not Config.API_KEY:
        pytest.skip("API_KEY not configured. Run get_api_key.py first")
    
    print(f"\nUsing API key: {Config.API_KEY[:20]}...")
    return APIClient(api_key=Config.API_KEY)

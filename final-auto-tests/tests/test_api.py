@"
import pytest
import allure
from api.client import APIClient
from api.endpoints import AuthEndpoints
from config.settings import Config

@allure.feature('API Tests')
@allure.story('Authentication API')
class TestAuthAPI:
    
    @allure.title('Test successful login via API')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    def test_login_success(self, api_client):
        response = api_client.post(AuthEndpoints.LOGIN, json={
            'email': Config.TEST_USER_EMAIL,
            'password': Config.TEST_USER_PASSWORD
        })
        
        assert response.status_code == 200, f'Expected 200, got {response.status_code}'
        response_data = response.json()
        assert 'token' in response_data, 'Response should contain token'
"@ | Out-File -FilePath tests\test_api.py -Encoding UTF8

@"
import pytest
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.test_data import TestData
from config.settings import Config

@allure.feature('UI Tests')
@allure.story('Authentication')
class TestAuthentication:
    
    @allure.title('Test successful login with valid credentials')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    def test_valid_login(self, browser):
        login_page = LoginPage(browser)
        login_page.open(Config.BASE_URL)
        login_page.login(Config.TEST_USER_EMAIL, Config.TEST_USER_PASSWORD)
        
        dashboard_page = DashboardPage(browser)
        assert dashboard_page.is_element_visible(dashboard_page.USER_MENU), 'Login failed - user menu not visible'
    
    @allure.title('Test login with invalid credentials')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    @pytest.mark.parametrize('credentials', TestData.INVALID_LOGIN)
    def test_invalid_login(self, browser, credentials):
        login_page = LoginPage(browser)
        login_page.open(Config.BASE_URL)
        login_page.login(credentials['email'], credentials['password'])
        
        error_message = login_page.get_error_message()
        assert credentials['error'] in error_message, f'Expected error: {credentials['error']}, got: {error_message}'
"@ | Out-File -FilePath tests\test_ui.py -Encoding UTF8

@"
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from api.client import APIClient
from pages.login_page import LoginPage
from config.settings import Config

@pytest.fixture(scope="function")
def browser():
    """Fixture for browser initialization"""
    options = Options()
    if Config.HEADLESS:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.maximize_window()
    
    yield driver
    
    driver.quit()

@pytest.fixture(scope="function")
def api_client():
    """Fixture for API client without auth"""
    return APIClient()

@pytest.fixture(scope="function")
def auth_api_client():
    """Fixture for API client with auth"""
    client = APIClient()
    response = client.post('/auth/login', json={
        'email': Config.TEST_USER_EMAIL,
        'password': Config.TEST_USER_PASSWORD
    })
    
    if response.status_code == 200:
        token = response.json().get('token')
        return APIClient(token=token)
    else:
        pytest.skip(f"Cannot authenticate via API: {response.status_code}")

@pytest.fixture(scope="function")
def authorized_user(browser):
    """Fixture for authorized user in UI tests"""
    login_page = LoginPage(browser)
    login_page.open(Config.BASE_URL)
    login_page.login(Config.TEST_USER_EMAIL, Config.TEST_USER_PASSWORD)
    return browser
"@ | Out-File -FilePath conftest.py -Encoding UTF8

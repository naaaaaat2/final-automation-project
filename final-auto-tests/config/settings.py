import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Base URLs
    BASE_URL = os.getenv('BASE_URL', 'https://yougile.com')
    API_URL = os.getenv('API_URL', 'https://yougile.com/api-v2')
    
    # Credentials - замените на свои тестовые данные
    TEST_USER_EMAIL = os.getenv('TEST_USER_EMAIL', 'your-test-email@example.com')
    TEST_USER_PASSWORD = os.getenv('TEST_USER_PASSWORD', 'your-password')
    
    # Browser settings
    BROWSER = os.getenv('BROWSER', 'chrome')
    HEADLESS = os.getenv('HEADLESS', 'False').lower() == 'true'
    IMPLICIT_WAIT = 10
    PAGE_LOAD_TIMEOUT = 30

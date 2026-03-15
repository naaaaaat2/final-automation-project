import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://yougile.com")
    API_URL = os.getenv("API_URL", "https://yougile.com/api-v2")
    TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL")
    TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD")
    TEST_COMPANY_ID = os.getenv("TEST_COMPANY_ID")
    API_KEY = os.getenv("API_KEY")
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
    IMPLICIT_WAIT = 10
    
    @classmethod
    def validate(cls):
        """Проверяет что все необходимые переменные окружения установлены"""
        required_vars = ['TEST_USER_EMAIL', 'TEST_USER_PASSWORD', 'TEST_COMPANY_ID']
        missing = [var for var in required_vars if not getattr(cls, var)]
        
        if missing:
            print(f"⚠️  Warning: Missing environment variables: {', '.join(missing)}")
            return False
        
        if not cls.API_KEY:
            print("⚠️  Warning: API_KEY not configured. Run get_api_key.py first")
        return True

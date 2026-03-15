@"
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    # Locators
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[type="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[type="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.error-message, .alert-danger')
    
    @allure.step('Login with credentials: {email}')
    def login(self, email, password):
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        self.wait_for_page_load()
    
    @allure.step('Get error message')
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
    
    @allure.step('Check if login successful')
    def is_login_successful(self):
        return not self.is_element_visible(self.ERROR_MESSAGE, timeout=3)
"@ | Out-File -FilePath pages\login_page.py -Encoding UTF8

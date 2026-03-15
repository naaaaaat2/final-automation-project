@"
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
from config.settings import Config

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.IMPLICIT_WAIT)
    
    @allure.step('Open page: {url}')
    def open(self, url):
        self.driver.get(url)
    
    @allure.step('Find element: {locator}')
    def find_element(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout or Config.IMPLICIT_WAIT)
        return wait.until(EC.presence_of_element_located(locator))
    
    @allure.step('Click element: {locator}')
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    @allure.step('Type text "{text}" to element: {locator}')
    def type_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step('Get text from element: {locator}')
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    @allure.step('Check if element is visible: {locator}')
    def is_element_visible(self, locator, timeout=None):
        try:
            wait = WebDriverWait(self.driver, timeout or Config.IMPLICIT_WAIT)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    @allure.step('Wait for page load')
    def wait_for_page_load(self):
        self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
"@ | Out-File -FilePath pages\base_page.py -Encoding UTF8

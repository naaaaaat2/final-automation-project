@"
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class DashboardPage(BasePage):
    # Locators
    CREATE_PROJECT_BUTTON = (By.CSS_SELECTOR, '[data-testid="create-project-button"], .btn-primary')
    PROJECT_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="name"], [placeholder*="название"]')
    CREATE_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    PROJECT_CARD = (By.CSS_SELECTOR, '.project-card, .board-item')
    USER_MENU = (By.CSS_SELECTOR, '.user-menu, .avatar')
    
    @allure.step('Create new project: {project_name}')
    def create_project(self, project_name):
        self.click(self.CREATE_PROJECT_BUTTON)
        self.type_text(self.PROJECT_NAME_INPUT, project_name)
        self.click(self.CREATE_BUTTON)
        self.wait_for_page_load()
    
    @allure.step('Check if project exists: {project_name}')
    def is_project_exists(self, project_name):
        projects = self.driver.find_elements(*self.PROJECT_CARD)
        for project in projects:
            if project_name in project.text:
                return True
        return False
"@ | Out-File -FilePath pages\dashboard_page.py -Encoding UTF8

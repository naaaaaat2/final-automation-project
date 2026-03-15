import random
from faker import Faker

fake = Faker()

class TestData:
    # Login test data
    VALID_LOGIN = {
        'email': 'your-test-email@example.com',  # Замените на реальный тестовый аккаунт
        'password': 'your-password'  # Замените на реальный пароль
    }
    
    INVALID_LOGIN = [
        {'email': 'wrong@email.com', 'password': 'wrongpass', 'error': 'Неверный email или пароль'},
        {'email': '', 'password': 'password123', 'error': 'Поле обязательно для заполнения'},
        {'email': 'test@test.com', 'password': '', 'error': 'Поле обязательно для заполнения'},
    ]
    
    @staticmethod
    def generate_project_name():
        """Generate unique project name for testing"""
        return f"Test Project {fake.word()} {random.randint(100, 999)}"
    
    @staticmethod
    def generate_task_title():
        """Generate unique task title for testing"""
        return f"Test Task {fake.sentence(nb_words=3)}"
    
    @staticmethod
    def generate_user_email():
        """Generate unique email for testing"""
        return fake.email()

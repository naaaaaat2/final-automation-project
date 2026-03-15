import random
from faker import Faker

fake = Faker()

class TestData:
    @staticmethod
    def generate_project_name():
        return f"Test Project {fake.word()} {random.randint(100, 999)}"
    
    @staticmethod
    def generate_task_title():
        return f"Test Task {fake.sentence(nb_words=3)}"
    
    @staticmethod
    def generate_company_id():
        return f"company_{random.randint(1000, 9999)}"

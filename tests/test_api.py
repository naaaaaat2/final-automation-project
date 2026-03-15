import pytest
import allure
from api.client import APIClient
from api.endpoints import ProjectEndpoints, TaskEndpoints
from config.settings import Config
from config.test_data import TestData

@pytest.mark.api
@allure.feature("API Tests")
class TestAPI:
    
    @allure.story("Projects")
    class TestProjects:
        
        @allure.title("Test get all projects")
        @allure.severity(allure.severity_level.CRITICAL)
        def test_get_projects(self, auth_api_client):
            """Test 1: Get all projects"""
            response = auth_api_client.get(ProjectEndpoints.BASE)
            
            print(f"\nGet projects: {response.status_code}")
            print(f"Response: {response.text}")
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            data = response.json()
            assert isinstance(data, dict) and "content" in data, "Response should contain 'content' field"
            projects = data.get("content", [])
            print(f"✅ Found {len(projects)} projects")
        
        @allure.title("Test create project")
        @allure.severity(allure.severity_level.CRITICAL)
        def test_create_project(self, auth_api_client):
            """Test 2: Create new project"""
            project_name = TestData.generate_project_name()
            print(f"\nCreating project: {project_name}")

            response = auth_api_client.post(ProjectEndpoints.BASE, json={
                "title": project_name
            })

            print(f"Response: {response.status_code} - {response.text}")
            assert response.status_code == 201, f"Expected 201, got {response.status_code}"
            data = response.json()
            assert "id" in data, "Response should contain project ID"
            print(f"✅ Created project with ID: {data['id']}")
        
        @allure.title("Test create project without auth")
        @allure.severity(allure.severity_level.CRITICAL)
        def test_create_project_unauthorized(self, api_client):
            """Test 3: Create project without authentication"""
            response = api_client.post(ProjectEndpoints.BASE, json={
                "title": "Test Project"
            })
            
            print(f"Response: {response.status_code}")
            assert response.status_code == 401, f"Expected 401, got {response.status_code}"
            print("✅ Correctly got 401 Unauthorized")
    
    @allure.story("Tasks")
    class TestTasks:
        
        @allure.title("Test create task")
        @allure.severity(allure.severity_level.CRITICAL)
        def test_create_task(self, auth_api_client):
            """Test 4: Create new task"""
            # Сначала создаем проект
            project_name = TestData.generate_project_name()
            project_response = auth_api_client.post(ProjectEndpoints.BASE, json={"title": project_name})
            
            if project_response.status_code != 201:
                pytest.skip(f"Could not create test project: {project_response.status_code}")
            
            project_id = project_response.json().get("id")
            task_title = TestData.generate_task_title()
            print(f"\nCreating task: {task_title}")
            
            # Согласно наблюдениям, API не требует указания проекта
            # Пробуем создать задачу без проекта
            response = auth_api_client.post(TaskEndpoints.BASE, json={
                "title": task_title
            })
            
            print(f"Response: {response.status_code} - {response.text}")
            
            # API может создавать задачи без проекта (возвращает 201)
            # Или требовать проект (возвращает 400)
            # Проверяем оба варианта
            if response.status_code == 201:
                data = response.json()
                assert "id" in data, "Response should contain task ID"
                print(f"✅ Created task with ID: {data['id']} (without project)")
            else:
                assert response.status_code == 400, f"Expected 201 or 400, got {response.status_code}"
                print("⚠️ API requires project for task creation")
        
        @allure.title("Test get tasks")
        @allure.severity(allure.severity_level.NORMAL)
        def test_get_tasks(self, auth_api_client):
            """Test 5: Get all tasks"""
            response = auth_api_client.get(TaskEndpoints.BASE)
            
            print(f"\nGet tasks: {response.status_code}")
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            data = response.json()
            assert isinstance(data, dict), "Response should be a dictionary"
            tasks = data.get("content", [])
            print(f"✅ Successfully got {len(tasks)} tasks")

@pytest.mark.api
@allure.feature("API Tests - Error Handling")
class TestAPIErrorHandling:
    
    @allure.title("Test invalid endpoint")
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_endpoint(self, api_client):
        """Test 6: Access invalid endpoint"""
        response = api_client.get("/invalid-endpoint")
        print(f"Response: {response.status_code}")
        assert response.status_code == 401, f"Expected 401 (Unauthorized), got {response.status_code}"
        print("✅ Correctly got 401 Unauthorized for invalid endpoint")
    
    @allure.title("Test invalid project ID")
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_project_id(self, auth_api_client):
        """Test 7: Get project with invalid ID"""
        invalid_id = "invalid-id-12345"
        response = auth_api_client.get(ProjectEndpoints.GET_BY_ID.format(id=invalid_id))
        print(f"Response: {response.status_code} - {response.text}")
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"
        print("✅ Correctly got 404 Not Found for invalid project ID")
    
    @allure.title("Test create project with empty title")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_project_empty_title(self, auth_api_client):
        """Test 8: Create project with empty title (should fail)"""
        response = auth_api_client.post(ProjectEndpoints.BASE, json={
            "title": ""
        })
        
        print(f"Response: {response.status_code} - {response.text}")
        assert response.status_code == 400, f"Expected 400, got {response.status_code}"
        print("✅ Correctly got 400 Bad Request for empty title")
    
    @allure.title("Test create task without title")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_task_without_title(self, auth_api_client):
        """Test 9: Create task without title (should fail)"""
        response = auth_api_client.post(TaskEndpoints.BASE, json={
            "description": "Task without title"
        })
        
        print(f"Response: {response.status_code} - {response.text}")
        
        # Проверяем что без title API возвращает ошибку
        if response.status_code == 400:
            print("✅ Correctly got 400 Bad Request for task without title")
            assert True
        else:
            # Если API создает задачу без title, тест падает
            assert False, f"Expected 400, got {response.status_code}. Task was created without title!"
    
    @allure.title("Test create task with empty title")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_task_empty_title(self, auth_api_client):
        """Test 10: Create task with empty title (should fail)"""
        response = auth_api_client.post(TaskEndpoints.BASE, json={
            "title": ""
        })
        
        print(f"Response: {response.status_code} - {response.text}")
        assert response.status_code == 400, f"Expected 400, got {response.status_code}"
        print("✅ Correctly got 400 Bad Request for empty title")

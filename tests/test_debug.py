import pytest
import requests
import json

def test_debug_login():
    """ростой тест для отладки логина"""
    url = "https://yougile.com/api-v2/auth/login"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    data = {
        "email": "your-test-email@example.com",  # амените на реальный email
        "password": "your-password"  # амените на реальный пароль
    }
    
    response = requests.post(url, headers=headers, json=data)
    print(f"\nStatus code: {response.status_code}")
    print(f"Response: {response.text}")
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

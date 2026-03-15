import requests
import json

def test_debug_login():
    """Debug test for login"""
    url = "https://yougile.com/api-v2/auth/login"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    # ЗАМЕНИТЕ НА ВАШИ РЕАЛЬНЫЕ ДАННЫЕ
    test_email = "your-real-email@example.com"  # <-- ВСТАВЬТЕ ВАШ EMAIL
    test_password = "your-real-password"        # <-- ВСТАВЬТЕ ВАШ ПАРОЛЬ
    
    data = {
        "email": test_email,
        "password": test_password
    }
    
    print(f"\nSending request to: {url}")
    print(f"Headers: {headers}")
    print(f"Data: {data}")
    
    response = requests.post(url, headers=headers, json=data)
    
    print(f"\nStatus code: {response.status_code}")
    print(f"Response headers: {dict(response.headers)}")
    print(f"Response body: {response.text}")
    
    if response.status_code == 200:
        print("✅ Login successful!")
    else:
        print("❌ Login failed")

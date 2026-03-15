# get_api_key.py
import requests
import json

def get_api_key(email, password, company_id):
    """
    Получает API-ключ для работы с YouGile API
    
    Args:
        email: ваш email в YouGile
        password: ваш пароль
        company_id: ID вашей компании
    
    Returns:
        API-ключ или None если не удалось получить
    """
    url = "https://yougile.com/api-v2/auth/keys"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "login": email,
        "password": password,
        "companyId": company_id
    }
    
    print(f"Отправка запроса к {url}")
    print(f"Данные: {data}")
    
    response = requests.post(url, headers=headers, json=data)
    
    print(f"Статус: {response.status_code}")
    print(f"Ответ: {response.text}")
    
    if response.status_code == 201:  # Created
        return response.json().get("key")
    
    return None

if __name__ == "__main__":
    # Ваши данные
    email = "nataliapavlyuk212@mail.ru"
    password = "Younata1997"
    company_id = "f6a8e686-b61a-4ebb-ad8b-2b4075d938c0"
    
    api_key = get_api_key(email, password, company_id)
    
    if api_key:
        print(f"\n✅ Ваш API-ключ: {api_key}")
        print("\nДобавьте эту строку в файл .env:")
        print(f"API_KEY={api_key}")
    else:
        print("\n❌ Не удалось получить API-ключ")

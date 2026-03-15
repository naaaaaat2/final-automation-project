@"
import requests
import allure
from config.settings import Config

class APIClient:
    def __init__(self, base_url=Config.API_URL, token=None):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        
        if token:
            self.session.headers.update({'Authorization': f'Bearer {token}'})
    
    @allure.step("API Request: {method} {endpoint}")
    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        
        allure.attach(
            f"Request: {method} {url}\nHeaders: {kwargs.get('headers', {})}\nBody: {kwargs.get('json', {})}",
            name="Request",
            attachment_type=allure.attachment_type.TEXT
        )
        
        allure.attach(
            f"Response: {response.status_code}\nBody: {response.text}",
            name="Response",
            attachment_type=allure.attachment_type.TEXT
        )
        
        return response
    
    def get(self, endpoint, **kwargs):
        return self.request('GET', endpoint, **kwargs)
    
    def post(self, endpoint, **kwargs):
        return self.request('POST', endpoint, **kwargs)
    
    def put(self, endpoint, **kwargs):
        return self.request('PUT', endpoint, **kwargs)
    
    def delete(self, endpoint, **kwargs):
        return self.request('DELETE', endpoint, **kwargs)
"@ | Out-File -FilePath api\client.py -Encoding UTF8

@"
class AuthEndpoints:
    LOGIN = '/auth/login'
    REGISTER = '/auth/register'
    
class ProjectEndpoints:
    BASE = '/projects'
    GET_BY_ID = '/projects/{id}'
    UPDATE = '/projects/{id}'
    DELETE = '/projects/{id}'

class TaskEndpoints:
    BASE = '/tasks'
    GET_BY_ID = '/tasks/{id}'
    UPDATE = '/tasks/{id}'
    DELETE = '/tasks/{id}'
"@ | Out-File -FilePath api\endpoints.py -Encoding UTF8

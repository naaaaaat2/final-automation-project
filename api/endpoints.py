class AuthEndpoints:
    COMPANIES_LIST = "/auth/companies"  # Получение списка компаний
    CREATE_KEY = "/auth/keys"            # Создание API-ключа
    GET_KEYS = "/auth/keys/get"          # Получение списка ключей
    DELETE_KEY = "/auth/keys/{id}"       # Удаление ключа
    
class ProjectEndpoints:
    BASE = "/projects"
    GET_BY_ID = "/projects/{id}"
    UPDATE = "/projects/{id}"
    DELETE = "/projects/{id}"

class TaskEndpoints:
    BASE = "/tasks"
    GET_BY_ID = "/tasks/{id}"
    UPDATE = "/tasks/{id}"
    DELETE = "/tasks/{id}"

# import httpx
#
# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
#
# print(response.status_code)  # 200
# print(response.json())       # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
from fileinput import close

# import httpx
#
# data = {
#     "title": "Новая задача",
#     "completed": False,
#     "userId": 1
# }
#
# response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
#
# print(response.status_code)  # 201 (Created)
# print(response.json())       # Ответ с созданной записью

# import httpx
#
# data = {"username": "test_user", "password": "123456"}
#
# response = httpx.post("https://httpbin.org/post", data=data)
#
# print(response.json())  # {'form': {'username': 'test_user', 'password': '123456'}, ...}

# import httpx
#
# headers = {"Authorization": "Bearer my_secret_token"}
#
# response = httpx.get("https://httpbin.org/get", headers=headers)
#
# print(response.json())  # Заголовки включены в ответ

# import httpx
#
# params = {"userId": 1}
#
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
#
# print(response.url)    # https://jsonplaceholder.typicode.com/todos?userId=1
# print(response.json()) # Фильтрованный список задач

# import httpx
#
# files = {"file": ("example.txt", open("example.txt", "rb"))}
#
# response = httpx.post("https://httpbin.org/post", files=files)
#
# print(response.json())  # Ответ с данными о загруженном файле

# import httpx
#
# with httpx.Client() as clients:
#     response1 = clients.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = clients.get("https://jsonplaceholder.typicode.com/todos/2")
#
# print(response1.json())  # Данные первой задачи
# print(response2.json())  # Данные второй задачи

# import httpx
#
# clients = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
#
# response = clients.get("https://httpbin.org/get")
#
# print(response.json())  # Заголовки включены в ответ
# clients.close()

# import httpx
#
# try:
#     response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
#     response.raise_for_status()  # Вызовет исключение при 4xx/5xx
# except httpx.HTTPStatusError as e:
#     print(f"Ошибка запроса: {e}")

# import httpx
#
# try:
#     response = httpx.get("https://httpbin.org/delay/5", timeout=2)
# except httpx.ReadTimeout:
#     print("Запрос превысил лимит времени")

# import httpx
#
# clients = httpx.Client(http2=True)
# response = clients.get("https://www.google.com")
#
# print(response.http_version)  # "HTTP/2"

# import requests
#
# try:
#     response = requests.get("https://jsonplaceholder.typicode.com/invalid-url")
#     response.raise_for_status()  # Поднимет исключение, если 4xx/5xx
# except requests.exceptions.HTTPError as e:
#     print(f"Ошибка: {e}")
# import httpx
#
# try:
#     response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
#     response.raise_for_status()  # Поднимет исключение, если 4xx/5xx
# except httpx.HTTPStatusError as e:
#     print(f"Ошибка: {e}")

import httpx

class UsersClient:
    def __init__(self, base_url: str):
        self.client = httpx.Client(base_url=base_url)

    def get_user(self, user_id: str):
        return self.client.get(f"/api/v1/users/{user_id}")

    def update_user(self, user_id: str, data: dict):
        return self.client.patch(f"/api/v1/users/{user_id}", json=data)

    def delete_user(self, user_id: str):
        return self.client.delete(f"/api/v1/users/{user_id}")

client = UsersClient(base_url="https://example.com")

user_id = ""
response1 = client.get_user(user_id)
response2 = client.update_user(user_id, {"email": "new@example.com"})
response3 = client.delete_user(user_id)



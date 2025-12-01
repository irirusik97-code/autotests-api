import httpx

# Проходим аутентификацию
login_payload = {
    "email": "JohnM@example.com",
    "password": "LLoo234!"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

# Инициализируем клиент с авторизацией
client = httpx.Client(base_url="http://localhost:8000",
                      timeout=100, # Таймаут в секундах
                      headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"})

response = client.get("/api/v1/users/me")

# Выводим ответ в консоль
print(response.text)
import httpx

payload_login = {
    "email": "JohnM@example.com",
    "password": "LLoo234!"
}

response_login = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload_login)
response_login_refresh_token = response_login.json()["token"]["refreshToken"]
response_login_access_token = response_login.json()["token"]["accessToken"]

print(response_login.status_code)
# print(response_login.json())

payload_refresh = {
    "refreshToken": response_login_refresh_token
}

response_refresh = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=payload_refresh)
# response_refresh_refresh_token = response_refresh.json()["token"]["refreshToken"]
# response_refresh_access_token = response_refresh.json()["token"]["accessToken"]

print(response_refresh.status_code)
# print(response_refresh.json())

# print(response_login_refresh_token == response_refresh_refresh_token)
# print(response_login_access_token == response_refresh_access_token)

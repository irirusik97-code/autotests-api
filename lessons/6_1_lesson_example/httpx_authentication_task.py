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
headers = {"Authorization": f"Bearer {response_login_access_token}"}

response_users_me = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
print(response_users_me.status_code)
print(response_users_me.json())

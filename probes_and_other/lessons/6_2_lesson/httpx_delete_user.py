import httpx
from tools.fakers import get_random_email

# step 1
users_payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

users_response = httpx.post("http://localhost:8000/api/v1/users", json=users_payload)
users_response_id = users_response.json()['user']['id']
print(users_response.json())
print(users_response.status_code)

# step 2
payload_login = {
    "email": users_payload['email'],
    "password": users_payload['password']
}

response_login = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload_login)
response_login_refresh_token = response_login.json()["token"]["refreshToken"]
response_login_access_token = response_login.json()["token"]["accessToken"]
print(response_login.json())
print(response_login.status_code)

# step 3
headers = {"Authorization": f"Bearer {response_login_access_token}"}

response_delete = httpx.delete(f"http://localhost:8000/api/v1/users/{users_response_id}", headers=headers)

print(response_delete.json())
print(response_delete.status_code)


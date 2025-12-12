from typing import TypedDict
from pydantic import BaseModel, EmailStr
from httpx import Client
from clients_2_0.authentication.authentication_client_2_0 import get_authentication_client #, LoginRequestDict
from clients_2_0.authentication.authentication_schema_2_0 import LoginRequestSchema


class AuthenticationUserSchema(BaseModel):
    email: EmailStr
    password: str


def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    The function creates an httpx.Client instance with user authentication.
    :return: A ready-to-use httpx.Client object.
    """
    # print('get_private_http_client() from private_http_builder_2_0')
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    authentication_client = get_authentication_client()
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )


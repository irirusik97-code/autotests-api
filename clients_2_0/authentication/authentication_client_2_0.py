import httpx
from clients_2_0.api_clients_2_0 import APIClient
from typing import TypedDict
from clients_2_0.public_http_builder_2_0 import get_public_http_client


class Token(TypedDict):
    """
    Description of the structure of authentication tokens. (using for LoginResponseDict)
    """
    tokenType: str
    accessToken: str
    refreshToken: str

class LoginRequestDict(TypedDict):
    """TypedDict for login_api"""
    email: str
    password: str

class RefreshTokenRequestDict(TypedDict):
    """TypedDict for refresh_token_api"""
    refreshToken: str

class LoginResponseDict(TypedDict):
    """TypedDict for login response"""
    token: Token



class AuthenticationClient(APIClient):
    """
    Client for work with /api/v1/authentication
    """
    def login_api(self, request: LoginRequestDict) -> httpx.Response:
        """
        The method performs user authentication.
        :param request: TypedDict with email and password.
        :return:Object Response with response data (httpx.Response object).
        """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_token_api(self, request: RefreshTokenRequestDict) -> httpx.Response:
        """
        The method updates the authorization token.
        :param request: TypedDict with refreshToken.
        :return:Object Response with response data (httpx.Response object).
        """
        return self.post("/api/v1/authentication/refresh", json=request)

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        """
        The method performs user authentication. (not API endpoint)
        :param request: TypedDict with email and password.
        :return: json with tokens
        """
        response = self.login_api(request)
        return response.json()


# builder for AuthenticationClient
def get_authentication_client() -> AuthenticationClient:
    """
    The function creates an AuthenticationClient instance with a pre-configured HTTP client.
    :return: A ready-to-use AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())




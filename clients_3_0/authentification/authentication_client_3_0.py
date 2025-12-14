import httpx
from clients_3_0.api_client_3_0 import APIClient
from clients_3_0.http_public_builder_3_0 import get_public_http_client
from clients_3_0.schema.all_schemas_3_0 import *

class AuthenticationClient(APIClient):
    """
    Client for work with /api/v1/authentication
    """
    def login_api(self, request: LoginRequestSchema) -> httpx.Response:
        """
        The method performs user authentication.
        :param request: TypedDict with email and password.
        :return:Object Response with response data (httpx.Response object).
        """
        return self.post("/api/v1/authentication/login", json=request.model_dump(by_alias=True)) # model_dump - convert to JSON, by_alias - convert from snake_case to camelCase

    def refresh_token_api(self, request: RefreshTokenRequestSchema) -> httpx.Response:
        """
        The method updates the authorization token.
        :param request: TypedDict with refreshToken.
        :return:Object Response with response data (httpx.Response object).
        """
        return self.post("/api/v1/authentication/refresh", json=request.model_dump(by_alias=True)) # model_dump - convert to JSON, by_alias - convert from snake_case to camelCase


# builder for AuthenticationClient
def get_authentication_client() -> AuthenticationClient:
    """
    The function creates an AuthenticationClient instance with a pre-configured HTTP client.
    :return: A ready-to-use AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())



import httpx
from clients_3_0.api_client_3_0 import APIClient
from clients_3_0.schema.all_schemas_3_0 import *
from clients_3_0.http_public_builder_3_0 import get_public_http_client

class PublicUsersClient(APIClient):
    """
    Client for work with /api/v1/users (only post user)
    """
    def create_user_api(self, request: CreateUserRequestSchema) -> httpx.Response:
        """
        The method performs creation of a new user.
        :param request: TypedDict with email, password, lastName, firstName, middleName.
        :return:Object Response with response data (httpx.Response object).
        """
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True)) # model_dump - convert to JSON, by_alias - convert from snake_case to camelCase

def get_public_users_client() -> PublicUsersClient:
    """
    The function creates an PublicUsersClient instance with a pre-configured HTTP client.
    :return: A ready-to-use PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())

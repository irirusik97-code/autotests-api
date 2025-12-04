import httpx
from clients_2_0.api_clients_2_0 import APIClient
from typing import TypedDict
from clients_2_0.public_http_builder_2_0 import get_public_http_client

class User(TypedDict):
    """
    Description of the user structure.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    """
    Description of the structure of the user creation response.
    """
    user: User

class CreateUserRequestDict(TypedDict):
    """
    Structure of the request to add a user.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Client for work with /api/v1/users (only post user)
    """
    def create_user_api(self, request: CreateUserRequestDict) -> httpx.Response:
        """
        The method performs creation of a new user.
        :param request: TypedDict with email, password, lastName, firstName, middleName.
        :return:Object Response with response data (httpx.Response object).
        """
        print('PublicUsersClient --> create_user_api() from public_users_client_2_0')
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        print('PublicUsersClient --> create_user() from public_users_client_2_0')
        response = self.create_user_api(request)
        return response.json()


def get_public_users_client() -> PublicUsersClient:
    """
    The function creates an PublicUsersClient instance with a pre-configured HTTP client.
    :return: A ready-to-use PublicUsersClient.
    """
    print('get_public_users_client() from public_users_client_2_0')
    return PublicUsersClient(client=get_public_http_client())


import httpx
from clients_3_0.api_client_3_0 import APIClient
from clients_3_0.schema.all_schemas_3_0 import *
from clients_3_0.http_private_builder_3_0 import get_private_http_client

class PrivateUsersClient(APIClient):
    """
    Client for work with /api/v1/users (for private requests)
    """
    def get_user_me_api(self) -> httpx.Response:
        """
        The method performs getting a current user.
        :return:Object Response with response data (httpx.Response object).
        """
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> httpx.Response:
        """
        The method performs getting a user by id.
        :param user_id: str with user_id
        :return:Object Response with response data (httpx.Response object).
        """
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> httpx.Response:
        """
        The method performs updating a user.
        :param user_id: str with user_id
        :param request: TypedDict with email, lastName, firstName, middleName.
        :return:Object Response with response data (httpx.Response object).
        """
        return self.patch(f"/api/v1/users/{user_id}",
                          json=request.model_dump(by_alias=True))

    def delete_user_api(self, user_id: str) -> httpx.Response:
        """
        The method performs deleting a user.
        :param user_id: str with user_id
        :return:Object Response with response data (httpx.Response object).
        """
        return self.delete(f"/api/v1/users/{user_id}")


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    The function creates an PrivateUsersClient instance with a pre-configured HTTP client.
    :return: A ready-to-use PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))

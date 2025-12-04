import httpx
from clients_2_0.api_clients_2_0 import APIClient

from clients_2_0.private_http_builder_2_0 import get_private_http_client, AuthenticationUserSchema

from clients_2_0.users.users_schema_2_0 import UpdateUserRequestSchema, GetUserResponseSchema

# class User(TypedDict):
#     """
#     Description of the user structure.
#     """
#     id: str
#     email: str
#     lastName: str
#     firstName: str
#     middleName: str
#
# class GetUserResponseDict(TypedDict):
#     """
#     Description of the structure of the user creation response.
#     """
#     user: User
#
# class UpdateUserRequestDict(TypedDict):
#     """
#     Structure of the request to update a user.
#     """
#     email: str | None
#     lastName: str | None
#     firstName: str | None
#     middleName: str | None

class PrivateUsersClient(APIClient):
    """
    Client for work with /api/v1/users (for private requests)
    """
    def get_user_me_api(self) -> httpx.Response:
        """
        The method performs getting a current user.
        :return:Object Response with response data (httpx.Response object).
        """
        print('PrivateUsersClient --> get_user_me_api() from private_users_client_2_0')
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> httpx.Response:
        """
        The method performs getting a user by id.
        :param user_id: str with user_id
        :return:Object Response with response data (httpx.Response object).
        """
        print('PrivateUsersClient --> get_user_api() from private_users_client_2_0')
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> httpx.Response:
        """
        The method performs updating a user.
        :param user_id: str with user_id
        :param request: TypedDict with email, lastName, firstName, middleName.
        :return:Object Response with response data (httpx.Response object).
        """
        print('PrivateUsersClient --> update_user_api() from private_users_client_2_0')
        return self.patch(f"/api/v1/users/{user_id}", json=request.model_dump(by_alias=True)) # Pydantic сам приводит имена полей в camelCase.

    def delete_user_api(self, user_id: str) -> httpx.Response:
        """
        The method performs deleting a user.
        :param user_id: str with user_id
        :return:Object Response with response data (httpx.Response object).
        """
        print('PrivateUsersClient --> delete_user_api() from private_users_client_2_0')
        return self.delete(f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        print('PrivateUsersClient --> get_user() from private_users_client_2_0')
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text) # автоматически преобразует JSON-строку в объект CourseSchema


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    The function creates an PrivateUsersClient instance with a pre-configured HTTP client.
    :return: A ready-to-use PrivateUsersClient.
    """
    print('get_private_users_client() from private_users_client_2_0')
    return PrivateUsersClient(client=get_private_http_client(user))


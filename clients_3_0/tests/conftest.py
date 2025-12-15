import pytest # Импортируем pytest
from pydantic import BaseModel, EmailStr
from clients_3_0.schema.all_schemas_3_0 import *

# Импортируем API клиенты
from clients_3_0.authentication.authentication_client_3_0 import AuthenticationClient, get_authentication_client
from clients_3_0.users.public_users_client_3_0 import get_public_users_client, PublicUsersClient
from tools.helpers.parsing_api_response import parse_api_response
from clients_3_0.users.private_users_client_3_0 import get_private_users_client, PrivateUsersClient


# Модель для агрегации возвращаемых данных фикстурой function_user
class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:  # Быстрый доступ к email пользователя
        return self.request.email

    @property
    def password(self) -> str:  # Быстрый доступ к password пользователя
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(email=self.email, password=self.password)


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def authentication_client() -> AuthenticationClient:  # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API клиент для работы с аутентификацией
    return get_authentication_client()


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def public_users_client() -> PublicUsersClient:  # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API клиент для работы с публичным API пользователей
    return get_public_users_client()

@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    return get_private_users_client(function_user.authentication_user)


# Фикстура для создания пользователя
@pytest.fixture
# Используем фикстуру public_users_client, которая создает нужный API клиент
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    create_user_api_request = CreateUserRequestSchema()
    create_user_api_response = public_users_client.create_user_api(create_user_api_request)
    pydantic_object_create_user_api_response = parse_api_response(CreateUserResponseSchema, create_user_api_response)

    return UserFixture(request=create_user_api_request,
                       response=pydantic_object_create_user_api_response)  # Возвращаем все нужные данные




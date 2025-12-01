from clients_2_0.private_http_builder_2_0 import AuthenticationUserDict
from clients_2_0.users.private_users_client_2_0 import get_private_users_client
from clients_2_0.users.public_users_client_2_0 import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
# Инициализируем клиент PrivateUsersClient
private_users_client = get_private_users_client(authentication_user)

# Отправляем GET запрос на получение данных пользователя
get_user_response = private_users_client.get_user_api(create_user_response_data['user']['id'])
get_user_response_data = get_user_response.json()
print('Get user data:', get_user_response_data)

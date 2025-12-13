# from clients_2_0.authentication.authentication_schema_2_0 import TokenSchema
#
# print(TokenSchema.model_json_schema())
import jsonschema
from clients_2_0.users.public_users_client_2_0 import get_public_users_client
from clients_2_0.users.users_schema_2_0 import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user_api(create_user_request)
# print(type(create_user_response.json()))
# Получаем JSON-схему из Pydantic-модели ответа
create_user_response_schema = CreateUserResponseSchema.model_json_schema()

# Проверяем, что JSON-ответ от API соответствует ожидаемой JSON-схеме
validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)


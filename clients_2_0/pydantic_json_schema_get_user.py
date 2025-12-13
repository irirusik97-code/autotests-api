import jsonschema
from clients_2_0.users.public_users_client_2_0 import get_public_users_client
from clients_2_0.users.users_schema_2_0 import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake
from clients_2_0.private_http_builder_2_0 import AuthenticationUserSchema
from clients_2_0.users.private_users_client_2_0 import get_private_users_client
from clients_2_0.users.users_schema_2_0 import GetUserResponseSchema

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

private_users_client = get_private_users_client(authentication_user)

get_user_response = private_users_client.get_user(create_user_response.user.id)
get_user_response_schema = GetUserResponseSchema.model_json_schema()

validate_json_schema(instance=get_user_response.model_dump(by_alias=True), schema=get_user_response_schema)



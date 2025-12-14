from clients_3_0.users.public_users_client_3_0 import get_public_users_client
from clients_3_0.users.private_users_client_3_0 import get_private_users_client
from clients_3_0.schema.all_schemas_3_0 import *
from tools.helpers.parsing_api_response import parse_api_response
from tools.assertions.schema import validate_json_schema

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema()

create_user_response_schema = CreateUserResponseSchema.model_json_schema()
get_user_response_schema = GetUserResponseSchema.model_json_schema()

create_user_api_response = public_users_client.create_user_api(create_user_request)
pydantic_object_create_user_api_response = parse_api_response(CreateUserResponseSchema, create_user_api_response)

print('Create user data:', pydantic_object_create_user_api_response)
validate_json_schema(instance=pydantic_object_create_user_api_response.model_dump(by_alias=True),
                     schema=create_user_response_schema)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

private_users_client = get_private_users_client(authentication_user)

get_user_api_response = private_users_client.get_user_api(pydantic_object_create_user_api_response.user.id)
pydantic_object_get_user_api_response = parse_api_response(GetUserResponseSchema, get_user_api_response)

print('Get user data:', pydantic_object_get_user_api_response)
validate_json_schema(instance=pydantic_object_get_user_api_response.model_dump(by_alias=True),
                     schema=get_user_response_schema)

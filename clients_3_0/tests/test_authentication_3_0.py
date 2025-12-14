from http import HTTPStatus

from clients_3_0.users.public_users_client_3_0 import get_public_users_client
from clients_3_0.authentication.authentication_client_3_0 import get_authentication_client
from clients_3_0.schema.all_schemas_3_0 import *
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.authentication import assert_login_response
import pytest

@pytest.mark.regression
@pytest.mark.authentication
def test_login():
    public_users_client = get_public_users_client()
    authentication_client = get_authentication_client()

    create_user_api_request = CreateUserRequestSchema()
    create_user_api_response = public_users_client.create_user_api(create_user_api_request)
    # pydantic_object_create_user_api_response = parse_api_response(CreateUserResponseSchema, create_user_api_response)

    login_request = LoginRequestSchema(
        email=create_user_api_request.email,
        password=create_user_api_request.password
    )

    login_api_response = authentication_client.login_api(login_request)
    login_api_response_data = LoginResponseSchema.model_validate_json(login_api_response.text)

    assert_status_code(login_api_response.status_code, HTTPStatus.OK)
    assert_login_response(login_api_response_data)

    validate_json_schema(login_api_response.json(),
                         login_api_response_data.model_json_schema())
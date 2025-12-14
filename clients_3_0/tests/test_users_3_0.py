from http import HTTPStatus

from clients_3_0.users.public_users_client_3_0 import get_public_users_client
from clients_3_0.schema.all_schemas_3_0 import *
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response
import pytest

@pytest.mark.users
@pytest.mark.regression
def test_create_user():
    public_users_client = get_public_users_client()

    create_user_api_request = CreateUserRequestSchema()
    create_user_api_response = public_users_client.create_user_api(create_user_api_request)
    create_user_api_response_data = CreateUserResponseSchema.model_validate_json(create_user_api_response.text)

    assert_status_code(create_user_api_response.status_code, HTTPStatus.OK)
    assert_create_user_response(create_user_api_request, create_user_api_response_data)

    validate_json_schema(create_user_api_response.json(), create_user_api_response_data.model_json_schema())


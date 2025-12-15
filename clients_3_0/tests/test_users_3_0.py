from http import HTTPStatus

from clients_3_0.users.public_users_client_3_0 import PublicUsersClient
from clients_3_0.schema.all_schemas_3_0 import *
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response
import pytest
from tools.helpers.parsing_api_response import parse_api_response

@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client: PublicUsersClient):
    # public_users_client = get_public_users_client() # changed to using fixture

    request = CreateUserRequestSchema() # create_user_api_request
    response = public_users_client.create_user_api(request) # create_user_api_response
    pydantic_object_response_data = parse_api_response(CreateUserResponseSchema, response)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_user_response(request, pydantic_object_response_data)

    validate_json_schema(response.json(), pydantic_object_response_data.model_json_schema())


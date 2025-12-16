from http import HTTPStatus

from clients_3_0.authentication.authentication_client_3_0 import AuthenticationClient
from clients_3_0.schema.all_schemas_3_0 import *
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.authentication import assert_login_response
import pytest
from clients_3_0.tests.conftest import UserFixture
from tools.helpers.parsing_api_response import parse_api_response

@pytest.mark.regression
@pytest.mark.authentication
def test_login(function_user: UserFixture, authentication_client: AuthenticationClient):

    request = LoginRequestSchema(email=function_user.email, password=function_user.password) # login_request

    response_object = authentication_client.login_api(request) # login_api_response
    response = parse_api_response(LoginResponseSchema, response_object)

    assert_status_code(response_object.status_code, HTTPStatus.OK)
    assert_login_response(response)

    validate_json_schema(response_object.json(),
                         response.model_json_schema())
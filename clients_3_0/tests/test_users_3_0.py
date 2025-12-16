from http import HTTPStatus

from clients_3_0.users.public_users_client_3_0 import PublicUsersClient
from clients_3_0.users.private_users_client_3_0 import PrivateUsersClient
from clients_3_0.schema.all_schemas_3_0 import *
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response, assert_get_user_response, assert_update_user_response
import pytest
from tools.helpers.parsing_api_response import parse_api_response
from clients_3_0.tests.conftest import UserFixture


@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client: PublicUsersClient):

    request = CreateUserRequestSchema() # create_user_api_request
    response_object = public_users_client.create_user_api(request) # create_user_api_response
    response = parse_api_response(CreateUserResponseSchema, response_object)

    assert_status_code(response_object.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response)

    validate_json_schema(response_object.json(), response.model_json_schema())


@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(function_user: UserFixture, private_users_client: PrivateUsersClient):

    response_object = private_users_client.get_user_me_api()
    response = parse_api_response(GetUserResponseSchema, response_object)

    assert_status_code(response_object.status_code, HTTPStatus.OK)

    assert_get_user_response(response, function_user.response)

    validate_json_schema(response_object.json(), response.model_json_schema())


@pytest.mark.users
@pytest.mark.regression
def test_get_user(function_user: UserFixture, private_users_client: PrivateUsersClient):

    response_object = private_users_client.get_user_api(function_user.response.user.id)
    response = parse_api_response(GetUserResponseSchema, response_object)

    assert_status_code(response_object.status_code, HTTPStatus.OK)
    assert_get_user_response(response, function_user.response)
    validate_json_schema(response_object.json(), response.model_json_schema())


@pytest.mark.users
@pytest.mark.regression
def test_update_user(function_user: UserFixture, private_users_client: PrivateUsersClient):
    update_request = UpdateUserRequestSchema()

    response_object = private_users_client.update_user_api(function_user.response.user.id, update_request)
    response = parse_api_response(GetUserResponseSchema, response_object)

    assert_status_code(response_object.status_code, HTTPStatus.OK)
    assert_update_user_response(update_request, response)
    validate_json_schema(response_object.json(), response.model_json_schema())


@pytest.mark.users
@pytest.mark.regression
def test_delete_user(function_user: UserFixture, private_users_client: PrivateUsersClient):

    response_object = private_users_client.delete_user_api(function_user.response.user.id)

    assert_status_code(response_object.status_code, HTTPStatus.OK)



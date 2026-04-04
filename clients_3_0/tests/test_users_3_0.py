from http import HTTPStatus

from clients_3_0.users.public_users_client_3_0 import PublicUsersClient
from clients_3_0.users.private_users_client_3_0 import PrivateUsersClient
from clients_3_0.schema.all_schemas_3_0 import *
# from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response, assert_get_user_response, assert_update_user_response
import pytest
from tools.helpers.parsing_api_response import parse_api_response
from clients_3_0.fixtures.users import UserFixture


# @pytest.mark.users
# @pytest.mark.regression
# def test_create_user(function_user: UserFixture):
#
#     assert_status_code(function_user.response_object.status_code, HTTPStatus.OK)
#     assert_create_user_response(function_user.request, function_user.response)


@pytest.mark.users
@pytest.mark.regression
@pytest.mark.parametrize("email", ["mail.ru", "gmail.com", "example.com"])
def test_create_user(email: str, public_users_client: PublicUsersClient):
    request = CreateUserRequestSchema(email=fake.email(domain=email))
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response_data)


@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(function_user: UserFixture, private_users_client: PrivateUsersClient):

    response_object = private_users_client.get_user_me_api()
    response = parse_api_response(GetUserResponseSchema, response_object)

    assert_status_code(response_object.status_code, HTTPStatus.OK)

    assert_get_user_response(response, function_user.response)

    # validate_json_schema(response_object.json(), response.model_json_schema())


@pytest.mark.users
@pytest.mark.regression
def test_get_user(function_user: UserFixture, private_users_client: PrivateUsersClient):

    response_object = private_users_client.get_user_api(function_user.response.user.id)
    response = parse_api_response(GetUserResponseSchema, response_object)

    assert_status_code(response_object.status_code, HTTPStatus.OK)
    assert_get_user_response(response, function_user.response)
    # validate_json_schema(response_object.json(), response.model_json_schema())


@pytest.mark.users
@pytest.mark.regression
def test_update_user(function_user: UserFixture, private_users_client: PrivateUsersClient):
    update_request = UpdateUserRequestSchema()

    response_object = private_users_client.update_user_api(function_user.response.user.id, update_request)
    response = parse_api_response(GetUserResponseSchema, response_object)

    assert_status_code(response_object.status_code, HTTPStatus.OK)
    assert_update_user_response(update_request, response)
    # validate_json_schema(response_object.json(), response.model_json_schema())


@pytest.mark.users
@pytest.mark.regression
def test_delete_user(function_user: UserFixture, private_users_client: PrivateUsersClient):

    response_object = private_users_client.delete_user_api(function_user.response.user.id)

    assert_status_code(response_object.status_code, HTTPStatus.OK)



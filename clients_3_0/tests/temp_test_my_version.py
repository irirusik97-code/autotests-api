import pytest
from clients_3_0.users.public_users_client_3_0 import get_public_users_client
from clients_3_0.users.private_users_client_3_0 import get_private_users_client
from clients_3_0.schema.all_schemas_3_0 import *
from tools.helpers.parsing_api_response import parse_api_response
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response, assert_get_user_response, assert_update_user_response
from http import HTTPStatus
from tools.assertions.schema import validate_json_schema

@pytest.mark.users
@pytest.mark.regression
def test_create_user():
    request = CreateUserRequestSchema()

    public_users_client = get_public_users_client()

    response_object = public_users_client.create_user_api(request)
    response = parse_api_response(CreateUserResponseSchema, response_object)

    assert_status_code(response_object.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response)
    validate_json_schema(response_object.json(), response.model_json_schema())

@pytest.mark.users
@pytest.mark.regression
def test_get_user_me():
    request = CreateUserRequestSchema()
    public_users_client = get_public_users_client()

    temp_response_object = public_users_client.create_user_api(request)
    temp_response = parse_api_response(CreateUserResponseSchema, temp_response_object)

    authentication_user = AuthenticationUserSchema(
        email=request.email,
        password=request.password
    )
    private_users_client = get_private_users_client(authentication_user)

    response_object = private_users_client.get_user_me_api()
    response = parse_api_response(GetUserResponseSchema, response_object)

    assert_status_code(response_object.status_code, HTTPStatus.OK)
    assert_get_user_response(response, temp_response)
    validate_json_schema(response_object.json(), response.model_json_schema())


@pytest.mark.users
@pytest.mark.regression
def test_get_user():
    request = CreateUserRequestSchema()
    public_users_client = get_public_users_client()

    temp_response_object = public_users_client.create_user_api(request)
    temp_response = parse_api_response(CreateUserResponseSchema, temp_response_object)

    authentication_user = AuthenticationUserSchema(
        email=request.email,
        password=request.password
    )
    private_users_client = get_private_users_client(authentication_user)

    response_object = private_users_client.get_user_api(temp_response.user.id)
    response = parse_api_response(GetUserResponseSchema, response_object)

    assert_status_code(response_object.status_code, HTTPStatus.OK)
    assert_get_user_response(response, temp_response)
    validate_json_schema(response_object.json(), response.model_json_schema())


@pytest.mark.users
@pytest.mark.regression
def test_update_user():
    request = CreateUserRequestSchema()
    public_users_client = get_public_users_client()

    temp_response_object = public_users_client.create_user_api(request)
    temp_response = parse_api_response(CreateUserResponseSchema, temp_response_object)

    authentication_user = AuthenticationUserSchema(
        email=request.email,
        password=request.password
    )
    private_users_client = get_private_users_client(authentication_user)

    update_request = UpdateUserRequestSchema()

    response_object = private_users_client.update_user_api(temp_response.user.id, update_request)
    response = parse_api_response(GetUserResponseSchema, response_object)

    assert_status_code(response_object.status_code, HTTPStatus.OK)
    assert_update_user_response(update_request, response)
    validate_json_schema(response_object.json(), response.model_json_schema())


@pytest.mark.users
@pytest.mark.regression
def test_delete_user():
    request = CreateUserRequestSchema()
    public_users_client = get_public_users_client()

    temp_response_object = public_users_client.create_user_api(request)
    temp_response = parse_api_response(CreateUserResponseSchema, temp_response_object)

    authentication_user = AuthenticationUserSchema(
        email=request.email,
        password=request.password
    )
    private_users_client = get_private_users_client(authentication_user)

    response_object = private_users_client.delete_user_api(temp_response.user.id)
    # print('test56')
    # print(response_object)
    # print(response_object.json())
    # response = parse_api_response(GetUserResponseSchema, response_object)
    assert_status_code(response_object.status_code, HTTPStatus.OK)
    # assert_update_user_response(update_request, response)
    # validate_json_schema(response_object.json(), response.model_json_schema())


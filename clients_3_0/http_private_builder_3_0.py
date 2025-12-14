from httpx import Client
from clients_3_0.schema.all_schemas_3_0 import *
from clients_3_0.authentification.authentication_client_3_0 import get_authentication_client
from tools.helpers.parsing_api_response import parse_api_response

# private
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    The function creates an httpx.Client instance with user authentication.
    :return: A ready-to-use httpx.Client object.
    """
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    authentication_client = get_authentication_client()
    login_api_response = authentication_client.login_api(login_request)
    pydantic_object_login_api_response = parse_api_response(LoginResponseSchema, login_api_response)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {pydantic_object_login_api_response.token.access_token}"}
    )
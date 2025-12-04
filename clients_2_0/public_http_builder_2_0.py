from httpx import Client


def get_public_http_client() -> Client:
    """
    The function creates an httpx.Client instance with basic settings.
    :return: A ready-to-use httpx.Client object.
    """
    print('get_public_http_client() from public_http_builder_2_0')
    return Client(timeout=100, base_url="http://localhost:8000")
from httpx import Client

# public
def get_public_http_client() -> Client:
    """
    The function creates an httpx.Client instance with basic settings.
    :return: A ready-to-use httpx.Client object.
    """
    return Client(timeout=100, base_url="http://localhost:8000")

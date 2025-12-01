import httpx
from typing import Any
from httpx._types import RequestData, RequestFiles

class APIClient:
    def __init__(self, client: httpx.Client):
        """
        Basic API Client, getting httpx.Client.
        :param client: httpx.Client instance for making HTTP requests
        """
        self.client = client

    def get(self, url: httpx.URL | str,
            params: httpx.QueryParams | None = None) -> httpx.Response:
        """
        GET-request.
        :param url: URL of endpoint.
        :param params: GET-parameters of request (for example, ?key=value).
        :return: Object Response with response data.
        """
        return self.client.get(url, params=params)


    def post(self, url: httpx.URL | str,
             params: httpx.QueryParams | None = None,
             json: Any | None = None,
             data: RequestData | None = None,
             files: RequestFiles | None = None, ) -> httpx.Response:
        """
        POST-request.
        :param url: URL of endpoint.
        :param params: parameters of request (for example, ?key=value).
        :param json: JSON data.
        :param data: Formatted form data (for example, application/x-www-form-urlencoded).
        :param files: Files to upload to the server.
        :return: Object Response with response data.
        """
        return self.client.post(url, params=params, json=json, data=data, files=files)


    def patch(self, url: httpx.URL | str,
             params: httpx.QueryParams | None = None,
             json: Any | None = None,
             data: RequestData | None = None) -> httpx.Response:
        """
        PATCH-request.
        :param url: URL of endpoint.
        :param params: parameters of request (for example, ?key=value).
        :param json: JSON data.
        :param data: Formatted form data (for example, application/x-www-form-urlencoded).
        :return: Object Response with response data.
        """
        return self.client.patch(url, params=params, json=json, data=data)


    def delete(self, url: httpx.URL | str,
               params: httpx.QueryParams | None=None,
               json: Any | None = None,
               data: RequestData | None = None) -> httpx.Response:
        """
        DELETE-request.
        :param url: URL of endpoint.
        :param params: parameters of request (for example, ?key=value).
        :param json: JSON data.
        :param data: Formatted form data (for example, application/x-www-form-urlencoded).
        :return: Object Response with response data.
        """
        return self.client.delete(url, params=params, json=json, data=data)


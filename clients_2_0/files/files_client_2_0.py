from typing import TypedDict
import httpx
from clients_2_0.api_clients_2_0 import APIClient
from clients_2_0.private_http_builder_2_0 import get_private_http_client, AuthenticationUserSchema

class File(TypedDict):
    """
    Description of the file structure.
    """
    id: str
    url: str
    filename: str
    directory: str

class CreateFileRequestDict(TypedDict):
    """
    Structure of a file creation request.
    """
    filename: str
    directory: str
    upload_file: str

class CreateFileResponseDict(TypedDict):
    """
    Description of the structure of the file creation response.
    """
    file: File


class FilesClient(APIClient):
    """
    Client for work with /api/v1/files
    """
    def get_file_api(self, file_id: str) -> httpx.Response:
        """
        The method performs getting a file by id.
        :param file_id: str with file_id
        :return:Object Response with response data (httpx.Response object).
        """
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> httpx.Response:
        """
        The method performs creating a file.
        :param request: TypedDict with filename, directory, upload_file.
        :return:Object Response with response data (httpx.Response object).
        """
        return self.post("/api/v1/files", data=request, files={"upload_file": open(request['upload_file'], 'rb')})

    def delete_file_api(self, file_id: str):
        """
        The method performs deleting a file by id.
        :param file_id: str with file_id
        :return:Object Response with response data (httpx.Response object).
        """
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponseDict:
        response = self.create_file_api(request)
        return response.json()

def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    The function creates an FilesClient instance with a pre-configured HTTP client.
    :return: A ready-to-use FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))


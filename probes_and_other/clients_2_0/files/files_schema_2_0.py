from pydantic import BaseModel, HttpUrl, Field
from tools.fakers import fake


class FileSchema(BaseModel):
    """
    Description of the file structure.
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str

class CreateFileRequestSchema(BaseModel):
    """
    Structure of a file creation request.
    """
    # Добавили генерацию случайного названия файла с расширением PNG
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    # Директорию оставляем статичной, чтобы все тестовые файлы на сервере попадали в одну папку
    directory: str = Field(default="tests")
    upload_file: str

class CreateFileResponseSchema(BaseModel):
    """
    Description of the structure of the file creation response.
    """
    file: FileSchema


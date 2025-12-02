import uuid

from pydantic import BaseModel, Field, EmailStr, HttpUrl

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    # in case when you need full name
    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"

class FileSchema(BaseModel):
    id: str
    url: HttpUrl = "http://localhost:8000"
    filename: str
    directory: str

class CourseSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    preview_file: FileSchema = Field(alias="previewFile") # Вложенная структура файла
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser") # Вложенная структура пользователя



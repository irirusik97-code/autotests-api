from pydantic import BaseModel, HttpUrl, Field, ConfigDict
from clients_2_0.files.files_schema_2_0 import FileSchema
from clients_2_0.users.users_schema_2_0 import UserSchema
from tools.fakers import fake

class CourseSchema(BaseModel):
    """
    Description of the course structure.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile") # Вложенная структура файла
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")  # Вложенная структура пользователя

class GetCoursesQuerySchema(BaseModel):
    """
    Structure of the request to get a list of courses.
    """
    user_id: str

class CreateCourseRequestSchema(BaseModel):
    """
    Structure of the request to create a course.
    """
    model_config = ConfigDict(populate_by_name=True)

    # Добавили генерацию случайного заголовка
    title: str = Field(default_factory=fake.sentence)
    # Добавили генерацию случайного максимального балла
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    # Добавили генерацию случайного минимального балла
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    # Добавили генерацию случайного описания
    description: str = Field(default_factory=fake.text)
    # Добавили генерацию случайного предполагаемого времени прохождения курса
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
    # Добавили генерацию случайного идентификатора файла
    preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uuid4)
    # Добавили генерацию случайного идентификатора пользователя
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4)

class UpdateCourseRequestSchema(BaseModel):
    """
    Structure of the request to update a course.
    """
    model_config = ConfigDict(populate_by_name=True)

    # Добавили генерацию случайного заголовка
    title: str | None = Field(default_factory=fake.sentence)
    # Добавили генерацию случайного максимального балла
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    # Добавили генерацию случайного минимального балла
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    # Добавили генерацию случайного описания
    description: str | None = Field(default_factory=fake.text)
    # Добавили генерацию случайного предполагаемого времени прохождения курса
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class CreateCourseResponseSchema(BaseModel):
    """
    Description of the structure of the course creation response.
    """
    course: CourseSchema
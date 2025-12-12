from pydantic import BaseModel, HttpUrl, Field, ConfigDict
from clients_2_0.files.files_schema_2_0 import FileSchema
from clients_2_0.users.users_schema_2_0 import UserSchema

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

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")

class UpdateCourseRequestSchema(BaseModel):
    """
    Structure of the request to update a course.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")

class CreateCourseResponseSchema(BaseModel):
    """
    Description of the structure of the course creation response.
    """
    course: CourseSchema
from pydantic import BaseModel, Field, EmailStr, ConfigDict, HttpUrl
from tools.fakers import fake


class AuthenticationUserSchema(BaseModel):
    email: EmailStr
    password: str

# authentication schemas
class TokenSchema(BaseModel): # inside response
    """
    Description of the structure of authentication tokens. (using for LoginResponseDict)
    """
    model_config = ConfigDict(populate_by_name=True)

    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginRequestSchema(BaseModel): # request
    """TypedDict for login_api"""
    email: str = Field(default_factory=fake.email)  # Добавили генерацию случайного email
    password: str = Field(default_factory=fake.password)  # Добавили генерацию случайного пароля

class RefreshTokenRequestSchema(BaseModel): # request
    """TypedDict for refresh_token_api"""
    model_config = ConfigDict(populate_by_name=True)

    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)

class LoginResponseSchema(BaseModel): # response
    """TypedDict for login response"""
    token: TokenSchema


# users schemas
class UserSchema(BaseModel): # inside response
    """
    Description of the user structure.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class GetUserResponseSchema(BaseModel): # response
    """
    Description of the structure of the user creation response.
    """
    user: UserSchema

class UpdateUserRequestSchema(BaseModel): # request
    """
    Structure of the request to update a user.
    """
    model_config = ConfigDict(populate_by_name=True)

    # Добавили генерацию случайного email
    email: EmailStr | None = Field(default_factory=fake.email)
    # Добавили генерацию случайной фамилии
    last_name: str | None = Field(alias="lastName", default_factory=fake.last_name)
    # Добавили генерацию случайного имени
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)
    # Добавили генерацию случайного отчества
    middle_name: str | None = Field(alias="middleName", default_factory=fake.middle_name)

class UpdateUserResponseSchema(BaseModel): # response
    """
    Description of the structure of the user updating response.
    """
    user: UserSchema

class CreateUserResponseSchema(BaseModel): # response
    """
    Description of the structure of the user creation response.
    """
    user: UserSchema

class CreateUserRequestSchema(BaseModel): # request
    """
    Structure of the request to add a user.
    """
    model_config = ConfigDict(populate_by_name=True)

    # Добавили генерацию случайного email
    email: EmailStr = Field(default_factory=fake.email)
    # Добавили генерацию случайного пароля
    password: str = Field(default_factory=fake.password)
    # Добавили генерацию случайной фамилии
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    # Добавили генерацию случайного имени
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    # Добавили генерацию случайного отчества
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)


# files schemas
class FileSchema(BaseModel): # inside response
    """
    Description of the file structure.
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str

class CreateFileRequestSchema(BaseModel): # request
    """
    Structure of a file creation request.
    """
    # Добавили генерацию случайного названия файла с расширением PNG
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    # Директорию оставляем статичной, чтобы все тестовые файлы на сервере попадали в одну папку
    directory: str = Field(default="tests")
    upload_file: str

class CreateFileResponseSchema(BaseModel): # response
    """
    Description of the structure of the file creation response.
    """
    file: FileSchema


# courses schemas
class CourseSchema(BaseModel): # inside response
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

class GetCoursesQuerySchema(BaseModel): # request
    """
    Structure of the request to get a list of courses.
    """
    user_id: str

class CreateCourseRequestSchema(BaseModel): # request
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

class UpdateCourseRequestSchema(BaseModel): # request
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

class CreateCourseResponseSchema(BaseModel): # response
    """
    Description of the structure of the course creation response.
    """
    course: CourseSchema


# exercises schemas
class ExerciseSchema(BaseModel): # inside response
    """
    Description of the exercise structure.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')

class GetExercisesQuerySchema(BaseModel): # request
    """
    Structure of the request to get a list of exercises.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str

class CreateExercisesRequestSchema(BaseModel):
    """
    Structure of the request to create an exercise.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias='courseId', default_factory=fake.uuid4)
    max_score: int = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int = Field(alias='minScore', default_factory=fake.min_score)
    order_index: int = Field(alias='orderIndex', default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias='estimatedTime', default_factory=fake.estimated_time)

class CreateExerciseResponseSchema(BaseModel): # response
    """
    Structure of the response to create an exercise.
    """
    exercise: ExerciseSchema

class UpdateExercisesRequestSchema(BaseModel): # request
    """
    Structure of the request to update an exercise.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=fake.min_score)
    order_index: int | None = Field(alias='orderIndex', default_factory=fake.integer)
    description: str | None
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)

class GetExercisesResponseSchema(BaseModel): # response
    """
    Description of the structure of the getting exercise response.
    """
    exercises: list[ExerciseSchema]



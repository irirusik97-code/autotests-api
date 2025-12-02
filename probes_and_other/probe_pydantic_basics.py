from pydantic import BaseModel


# class CourseSchema(BaseModel):
#     id: str
#     title: str
#     maxScore: int
#     minScore: int
#     description: str
#     estimatedTime: str


# # Инициализируем модель CourseSchema через передачу аргументов
# course_default_model = CourseSchema(
#     id="course-id",
#     title="Playwright",
#     maxScore=100,
#     minScore=10,
#     description="Playwright",
#     estimatedTime="1 week"
# )
# print('Course default model:', course_default_model)

# # Инициализируем модель CourseSchema через распаковку словаря
# course_dict = {
#     "id": "course-id",
#     "title": "Playwright",
#     "maxScore": 100,
#     "minScore": 10,
#     "description": "Playwright",
#     "estimatedTime": "1 week"
# }
# course_dict_model = CourseSchema(**course_dict)
# print('Course dict model:', course_dict_model)

# Инициализируем модель CourseSchema через JSON
# course_json = """
# {
#     "id": "course-id",
#     "title": "Playwright",
#     "maxScore": 100,
#     "minScore": 10,
#     "description": "Playwright",
#     "estimatedTime": "1 week"
# }
# """
# course_json_model = CourseSchema.model_validate_json(course_json)
# print('Course JSON model:', course_json_model)

# import json
#
# with open("course.json", "r") as file:
#     course_data = file.read()
#
# course_model = CourseSchema.model_validate_json(course_data)
# print(course_model)

#
# from pydantic import BaseModel, Field
#
#
# class CourseSchema(BaseModel):
#     id: str
#     title: str
#     max_score: int = Field(alias="maxScore")
#     min_score: int = Field(alias="minScore")
#     description: str
#     estimated_time: str = Field(alias="estimatedTime")
#
# course_dict = {
#     "id": "course-id",
#     "title": "Playwright",
#     "maxScore": 100,
#     "minScore": 10,
#     "description": "Playwright",
#     "estimatedTime": "1 week"
# }
# course_dict_model = CourseSchema(**course_dict)
# print(course_dict_model.model_dump(by_alias=False))
# print(course_dict_model.model_dump(by_alias=True))


# from pydantic import BaseModel, ConfigDict
# from pydantic.alias_generators import to_camel
#
#
# class CourseSchema(BaseModel):
#     # Автоматическое преобразование snake_case → camelCase
#     model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
#
#     id: str
#     title: str
#     max_score: int
#     min_score: int
#     description: str
#     estimated_time: str
#
#
# course_data = {
#     "id": "course-id",
#     "title": "Playwright",
#     "maxScore": 100,
#     "minScore": 10,
#     "description": "Playwright",
#     "estimatedTime": "1 week"
# }
#
# course_model = CourseSchema(**course_data)
# print(course_model.model_dump(by_alias=True))


# from pydantic import BaseModel, Field
#
#
# class CourseSchema(BaseModel):
#     id: str = "course-id"
#     title: str = "Playwright"
#     max_score: int = Field(alias="maxScore", default=1000)
#     min_score: int = Field(alias="minScore", default=100)
#     description: str = "Playwright course"
#     estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
#
# # Создадим объект модели без передачи параметров
# course = CourseSchema()
# print(course)

# import uuid
# from pydantic import BaseModel, Field
#
#
# class CourseSchema(BaseModel):
#     id: str = Field(default_factory=lambda: str(uuid.uuid4()))
#     title: str = "Playwright"
#     max_score: int = Field(alias="maxScore", default=1000)
#     min_score: int = Field(alias="minScore", default=100)
#     description: str = "Playwright course"
#     estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
#
#
# # Создадим несколько объектов модели
# course1 = CourseSchema()
# course2 = CourseSchema()
#
# print(course1.id)
# print(course2.id)


# import uuid
#
# from pydantic import BaseModel, Field, HttpUrl, EmailStr, ValidationError
#
#
# # Добавили модель FileSchema
# class FileSchema(BaseModel):
#     id: str
#     url: HttpUrl  # Используем HttpUrl вместо str
#     filename: str
#     directory: str
#
#
# # Добавили модель UserSchema
# class UserSchema(BaseModel):
#     id: str
#     email: EmailStr  # Используем EmailStr вместо str
#     last_name: str = Field(alias="lastName")
#     first_name: str = Field(alias="firstName")
#     middle_name: str = Field(alias="middleName")
#
#     def get_username(self) -> str:
#         return f"{self.first_name} {self.last_name}"
#
# class CourseSchema(BaseModel):
#     id: str = Field(default_factory=lambda: str(uuid.uuid4()))
#     title: str = "Playwright"
#     max_score: int = Field(alias="maxScore", default=1000)
#     min_score: int = Field(alias="minScore", default=100)
#     description: str = "Playwright course"
#     preview_file: FileSchema = Field(alias="previewFile") # Вложенная структура файла
#     estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
#     created_by_user: UserSchema = Field(alias="createdByUser") # Вложенная структура пользователя


# # Инициализируем модель CourseSchema через передачу аргументов
# course_default_model = CourseSchema(
#     id="course-id",
#     title="Playwright",
#     maxScore=100,
#     minScore=10,
#     description="Playwright",
#     # Добавили инициализацию вложенной модели FileSchema
#     previewFile=FileSchema(
#         id="file-id",
#         url="http://localhost:8000",
#         filename="file.png",
#         directory="courses",
#     ),
#     estimatedTime="1 week",
#     # Добавили инициализацию вложенной модели UserSchema
#     createdByUser=UserSchema(
#         id="user-id",
#         email="user@gmail.com",
#         lastName="Bond",
#         firstName="Zara",
#         middleName="Alise"
#     )
# )
# print('Course default model:', course_default_model)

# # Инициализируем модель CourseSchema через распаковку словаря
# course_dict = {
#     "id": "course-id",
#     "title": "Playwright",
#     "maxScore": 100,
#     "minScore": 10,
#     "description": "Playwright",
#     # Добавили ключ previewFile
#     "previewFile": {
#         "id": "file-id",
#         "url": "http://localhost:8000",
#         "filename": "file.png",
#         "directory": "courses"
#     },
#     "estimatedTime": "1 week",
#     # Добавили ключ createdByUser
#     "createdByUser": {
#         "id": "user-id",
#         "email": "user@gmail.com",
#         "lastName": "Bond",
#         "firstName": "Zara",
#         "middleName": "Alise"
#     }
# }
# course_dict_model = CourseSchema(**course_dict)
# print('Course dict model:', course_dict_model)

# Инициализируем модель CourseSchema через JSON
# course_json = """
# {
#     "id": "course-id",
#     "title": "Playwright",
#     "maxScore": 100,
#     "minScore": 10,
#     "description": "Playwright",
#     "previewFile": {
#         "id": "file-id",
#         "url": "http://localhost:8000",
#         "filename": "file.png",
#         "directory": "courses"
#     },
#     "estimatedTime": "1 week",
#     "createdByUser": {
#         "id": "user-id",
#         "email": "user@gmail.com",
#         "lastName": "Bond",
#         "firstName": "Zara",
#         "middleName": "Alise"
#     }
# }
# """
# course_json_model = CourseSchema.model_validate_json(course_json)
# print('Course JSON model:', course_json_model)

# file = FileSchema(
#     id="file-id",
#     url="localhost",
#     filename="file.png",
#     directory="courses",
# )
#
# # Инициализируем FileSchema c некорректным url
# try:
#     file = FileSchema(
#         id="file-id",
#         url="localhost",
#         filename="file.png",
#         directory="courses",
#     )
# except ValidationError as error:
#     print(error)
#     print(error.errors())

import uuid

from pydantic import BaseModel, Field, EmailStr, HttpUrl, ValidationError


# Добавили модель FileSchema
class FileSchema(BaseModel):
    id: str
    url: HttpUrl  # Используем HttpUrl вместо str
    filename: str
    directory: str


# Добавили модель UserSchema
class UserSchema(BaseModel):
    id: str
    email: EmailStr  # Используем EmailStr вместо str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CourseSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    # Вложенный объект для файла-превью
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    # Вложенный объект для пользователя, создавшего курс
    created_by_user: UserSchema = Field(alias="createdByUser")


# Инициализируем модель CourseSchema через передачу аргументов
course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    # Добавили инициализацию вложенной модели FileSchema
    previewFile=FileSchema(
        id="file-id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses",
    ),
    estimatedTime="1 week",
    # Добавили инициализацию вложенной модели UserSchema
    createdByUser=UserSchema(
        id="user-id",
        email="user@gmail.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alise"
    )
)
print('Course default model:', course_default_model)

# Инициализируем модель CourseSchema через распаковку словаря
course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    # Добавили ключ previewFile
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    # Добавили ключ createdByUser
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)
print(course_dict_model.model_dump())
print(course_dict_model.model_dump(by_alias=True))

# Инициализируем модель CourseSchema через JSON
course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print('Course JSON model:', course_json_model)

# Инициализируем FileSchema c некорректным url
try:
    file = FileSchema(
        id="file-id",
        url="localhost",
        filename="file.png",
        directory="courses",
    )
except ValidationError as error:
    print(error)
    print(error.errors())



import httpx
from clients_2_0.api_clients_2_0 import APIClient
from typing import TypedDict
from clients_2_0.private_http_builder_2_0 import get_private_http_client, AuthenticationUserSchema
# from clients_2_0.files.files_client_2_0 import File
from clients_2_0.files.files_schema_2_0 import FileSchema
from clients_2_0.users.users_schema_2_0 import UserSchema


class Course(TypedDict):
    """
    Description of the course structure.
    """
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: FileSchema  # Вложенная структура файла
    estimatedTime: str
    createdByUser: UserSchema  # Вложенная структура пользователя

class GetCoursesQueryDict(TypedDict):
    """
    Structure of the request to get a list of courses.
    """
    user_id: str

class CreateCourseRequestDict(TypedDict):
    """
    Structure of the request to create a course.
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateCourseRequestDict(TypedDict):
    """
    Structure of the request to update a course.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class CreateCourseResponseDict(TypedDict):
    """
    Description of the structure of the course creation response.
    """
    course: Course


class CoursesClient(APIClient):
    """
    Client for work with /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQueryDict) -> httpx.Response:
        """
        The method performs getting a list of courses by user id.
        :param query: TypedDict with user_id
        :return:Object Response with response data (httpx.Response object).
        """
        return self.get("/api/v1/courses", params=query)

    def get_course_api(self, course_id: str) -> httpx.Response:
        """
        The method performs getting a course by user id.
        :param course_id: str with course_id
        :return:Object Response with response data (httpx.Response object).
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestDict) -> httpx.Response:
        """
        The method performs creating a course.
        :param request: TypedDict with title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return:Object Response with response data (httpx.Response object).
        """
        return self.post("/api/v1/courses", json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> httpx.Response:
        """
        The method performs updating a course.
        :param course_id: str with course_id
        :param request: TypedDict with title, maxScore, minScore, description, estimatedTime.
        :return:Object Response with response data (httpx.Response object).
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> httpx.Response:
        """
        The method performs deleting a course by course id.
        :param course_id: str with course_id
        :return:Object Response with response data (httpx.Response object).
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestDict) -> CreateCourseResponseDict:
        response = self.create_course_api(request)
        return response.json()


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    The function creates an CoursesClient instance with a pre-configured HTTP client.
    :return: A ready-to-use CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))
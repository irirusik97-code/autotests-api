import httpx
from clients_3_0.api_client_3_0 import APIClient
from clients_3_0.schema.all_schemas_3_0 import *
from clients_3_0.http_private_builder_3_0 import get_private_http_client


class CoursesClient(APIClient):
    """
    Client for work with /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQuerySchema) -> httpx.Response:
        """
        The method performs getting a list of courses by user id.
        :param query: TypedDict with user_id
        :return:Object Response with response data (httpx.Response object).
        """
        return self.get("/api/v1/courses", params=query.model_dump(by_alias=True))

    def get_course_api(self, course_id: str) -> httpx.Response:
        """
        The method performs getting a course by user id.
        :param course_id: str with course_id
        :return:Object Response with response data (httpx.Response object).
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestSchema) -> httpx.Response:
        """
        The method performs creating a course.
        :param request: TypedDict with title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return:Object Response with response data (httpx.Response object).
        """
        return self.post("/api/v1/courses", json=request.model_dump(by_alias=True))

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> httpx.Response:
        """
        The method performs updating a course.
        :param course_id: str with course_id
        :param request: TypedDict with title, maxScore, minScore, description, estimatedTime.
        :return:Object Response with response data (httpx.Response object).
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request.model_dump(by_alias=True))

    def delete_course_api(self, course_id: str) -> httpx.Response:
        """
        The method performs deleting a course by course id.
        :param course_id: str with course_id
        :return:Object Response with response data (httpx.Response object).
        """
        return self.delete(f"/api/v1/courses/{course_id}")


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    The function creates an CoursesClient instance with a pre-configured HTTP client.
    :return: A ready-to-use CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))
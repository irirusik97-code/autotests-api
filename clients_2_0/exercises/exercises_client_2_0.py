import httpx
from clients_2_0.api_clients_2_0 import APIClient
from typing import TypedDict
from clients_2_0.private_http_builder_2_0 import get_private_http_client, AuthenticationUserDict

class GetExercisesQueryDict(TypedDict):
    """
    Structure of the request to get a list of exercises.
    """
    course_id: str

class CreateExercisesRequestDict(TypedDict):
    """
    Structure of the request to create an exercise.
    """
    title: str
    courseId: int
    maxScore: int
    minScore: str
    orderIndex: str
    description: str
    estimatedTime: str

class UpdateExercisesRequestDict(TypedDict):
    """
    Structure of the request to update an exercise.
    """
    title: str
    maxScore: int
    minScore: str
    orderIndex: str
    description: str
    estimatedTime: str

class ExercisesClient(APIClient):
    """
    Client for work with /api/v1/exercises
    """

    def get_courses_api(self, query: GetExercisesQueryDict) -> httpx.Response:
        """
        The method performs getting a list of exercises by course id.
        :param query: TypedDict with course_id
        :return:Object Response with response data (httpx.Response object).
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id : str) -> httpx.Response:
        """
        The method performs getting an exercise by exercise id.
        :param exercise_id: str with exercise_id
        :return:Object Response with response data (httpx.Response object).
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> httpx.Response:
        """
        The method performs creating an exercise.
        :param request: TypedDict with title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return:Object Response with response data (httpx.Response object).
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id : str, request: UpdateExercisesRequestDict) -> httpx.Response:
        """
        The method performs updating an exercise.
        :param exercise_id: str with exercise_id
        :param request: TypedDict with title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return:Object Response with response data (httpx.Response object).
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id : str) -> httpx.Response:
        """
        The method performs deleting an exercise by exercise id.
        :param exercise_id: str with exercise_id
        :return:Object Response with response data (httpx.Response object).
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")


def get_courses_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    The function creates an ExercisesClient instance with a pre-configured HTTP client.
    :return: A ready-to-use ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))

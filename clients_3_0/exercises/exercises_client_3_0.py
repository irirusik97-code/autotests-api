import httpx
from clients_3_0.api_client_3_0 import APIClient
from clients_3_0.schema.all_schemas_3_0 import *
from clients_3_0.http_private_builder_3_0 import get_private_http_client

class ExercisesClient(APIClient):
    """
    Client for work with /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> httpx.Response:
        """
        The method performs getting a list of exercises by course id.
        :param query: TypedDict with course_id
        :return:Object Response with response data (httpx.Response object).
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id : str) -> httpx.Response:
        """
        The method performs getting an exercise by exercise id.
        :param exercise_id: str with exercise_id
        :return:Object Response with response data (httpx.Response object).
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExercisesRequestSchema) -> httpx.Response:
        """
        The method performs creating an exercise.
        :param request: TypedDict with title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return:Object Response with response data (httpx.Response object).
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id : str, request: UpdateExercisesRequestSchema) -> httpx.Response:
        """
        The method performs updating an exercise.
        :param exercise_id: str with exercise_id
        :param request: TypedDict with title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return:Object Response with response data (httpx.Response object).
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id : str) -> httpx.Response:
        """
        The method performs deleting an exercise by exercise id.
        :param exercise_id: str with exercise_id
        :return:Object Response with response data (httpx.Response object).
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    The function creates an ExercisesClient instance with a pre-configured HTTP client.
    :return: A ready-to-use ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))


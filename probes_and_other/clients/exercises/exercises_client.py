from typing import TypedDict

from httpx import Response

from probes_and_other.clients.api_client import APIClient


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений
    """
    courseId: str


class GetExerciseQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений
    """
    exercise_id: str


class CreateExerciseQueryDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseQueryDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercise
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка упражнений для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации по конкретному заданию.

        :param query: Словарь с exercise_id.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseQueryDict) -> Response:
        """
        Метод создания задания.

        :param query: Словарь с Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime,
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseQueryDict) -> Response:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор упражнения.
        :param query: Словарь с Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime,
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор упражнения.
        :param query: Словарь с Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime,
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")


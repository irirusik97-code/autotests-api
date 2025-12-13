from pydantic import BaseModel, HttpUrl, Field, ConfigDict
from tools.fakers import fake

class ExerciseSchema(BaseModel):
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

class GetExercisesQuerySchema(BaseModel):
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

class CreateExerciseResponseSchema(BaseModel):
    """
    Structure of the response to create an exercise.
    """
    exercise: ExerciseSchema

class UpdateExercisesRequestSchema(BaseModel):
    """
    Structure of the request to update an exercise.
    """
    title: str
    max_score: int | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=fake.min_score)
    order_index: int | None = Field(alias='orderIndex', default_factory=fake.integer)
    description: str | None
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)

class GetExercisesResponseSchema(BaseModel):
    """
    Description of the structure of the getting exercise response.
    """
    exercises: list[ExerciseSchema]
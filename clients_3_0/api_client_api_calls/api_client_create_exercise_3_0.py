from clients_3_0.users.public_users_client_3_0 import get_public_users_client
from clients_3_0.schema.all_schemas_3_0 import *
from tools.helpers.parsing_api_response import parse_api_response
from clients_3_0.files.files_client_3_0 import get_files_client
from clients_3_0.courses.courses_client_3_0 import get_courses_client
from clients_3_0.exercises.exercises_client_3_0 import get_exercises_client

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema()

create_user_api_response = public_users_client.create_user_api(create_user_request)
pydantic_object_create_user_api_response = parse_api_response(CreateUserResponseSchema, create_user_api_response)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

create_file_api_request = CreateFileRequestSchema(upload_file="../../testdata/files/image.png")
create_file_api_response = files_client.create_file_api(create_file_api_request)
pydantic_object_create_file_api_response = parse_api_response(CreateFileResponseSchema, create_file_api_response)

create_course_api_request = CreateCourseRequestSchema(
    preview_file_id=pydantic_object_create_file_api_response.file.id,
    created_by_user_id=pydantic_object_create_user_api_response.user.id
)

create_course_api_response = courses_client.create_course_api(create_course_api_request)
pydantic_object_create_course_api_response = parse_api_response(CreateCourseResponseSchema, create_course_api_response)


create_exercise_api_request = CreateExercisesRequestSchema(
    courseId=pydantic_object_create_course_api_response.course.id
)
create_exercise_api_response = exercises_client.create_exercise_api(create_exercise_api_request)
pydantic_object_create_exercise_api_response = parse_api_response(CreateExerciseResponseSchema, create_exercise_api_response)
print('Create exercise data:', pydantic_object_create_exercise_api_response)

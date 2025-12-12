from clients_2_0.courses.courses_client_2_0 import get_courses_client, CreateCourseRequestDict
from clients_2_0.exercises.exercises_client_2_0 import get_exercises_client, CreateExercisesRequestDict
from clients_2_0.files.files_client_2_0 import get_files_client
from clients_2_0.files.files_schema_2_0 import CreateFileRequestSchema
from clients_2_0.private_http_builder_2_0 import AuthenticationUserSchema
from clients_2_0.users.public_users_client_2_0 import get_public_users_client
from clients_2_0.users.users_schema_2_0 import CreateUserRequestSchema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем клиенты
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

# Загружаем файл
create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="../testdata/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)
# print('Create file data:', create_file_response)

# Создаем курс
create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
# print('Create course data:', create_course_response)

# Создаем задание
create_exercise_request = CreateExercisesRequestDict(
    title="Exercise 1",
    courseId=create_course_response['course']['id'],
    maxScore=5,
    minScore=1,
    orderIndex=0,
    description="Exercise 1",
    estimatedTime="5 minutes"
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)

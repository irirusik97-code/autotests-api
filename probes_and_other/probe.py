# import asyncio
#
# async def fetch_data():
#     print("Начинаем загрузку...")
#     await asyncio.sleep(2)  # Имитация задержки I/O
#     print("Данные загружены")
#     return {"data": "Пример данных"}
#
# async def main():
#     result = await fetch_data()
#     print(result)
#
# asyncio.run(main())

# {
#   "email": "JohnM@example.com",
#   "password": "LLoo234!",
#   "lastName": "Malc",
#   "firstName": "John",
#   "middleName": "Cristian"
# }

# class Car:
#     def __init__(self, engine, wheels, color):
#         self.engine = engine
#         self.wheels = wheels
#         self.color = color
#
# class CarBuilder:
#     def __init__(self):
#         self.engine = None
#         self.wheels = 4
#         self.color = "white"
#
#     def set_engine(self, engine):
#         self.engine = engine
#         return self
#
#     def set_color(self, color):
#         self.color = color
#         return self
#
#     def build(self):
#         return Car(self.engine, self.wheels, self.color)
#
# # Использование:
# builder = CarBuilder()
# car = builder.set_engine("V8").set_color("red").build()
# print(car.color)


# from pydantic import BaseModel
#
# class User(BaseModel):
#     id: int
#     name: str
#     email: str
#     is_active: bool = True # Значение по умолчанию
#
# user = User(id=1, name="Alice", email="alice@example.com") # User(id="123", name="Alice") # 123 (автоматически преобразован в int)
# print(user)
# print(user.model_dump_json())  # Выводит JSON-строку
#
# class Address(BaseModel):
#     city: str
#     zip_code: str
#
# class User(BaseModel):
#     id: int
#     name: str
#     address: Address  # Вложенная модель
#
# user = User(id=1, name="Alice", address={"city": "New York", "zip_code": "10001"})
# print(user.address.city)  # "New York"


from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


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

# from jsonschema import validate, ValidationError
#
# # Пример схемы
# schema = {
#   "type": "object",
#   "properties": {
#     "name": { "type": "string" },
#     "age": { "type": "number" }
#   },
#   "required": ["name"]
# }
#
# # Пример данных
# data = {
#   "name": "John Doe",
#   "age": 30
# }
#
# try:
#     validate(instance=data, schema=schema)
#     print("Данные соответствуют схеме.")
# except ValidationError as e:
#     print(f"Ошибка валидации: {e.message}")


from jsonschema import validate
from jsonschema.validators import Draft202012Validator

schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "age": {"type": "integer"}
    },
    "required": ["id", "email"]
}

response = {
    "id": "12345",
    "email": "user-email",
    "age": 25
}

validate(instance=response, schema=schema, format_checker=Draft202012Validator.FORMAT_CHECKER)


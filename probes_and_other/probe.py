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

class Car:
    def __init__(self, engine, wheels, color):
        self.engine = engine
        self.wheels = wheels
        self.color = color

class CarBuilder:
    def __init__(self):
        self.engine = None
        self.wheels = 4
        self.color = "white"

    def set_engine(self, engine):
        self.engine = engine
        return self

    def set_color(self, color):
        self.color = color
        return self

    def build(self):
        return Car(self.engine, self.wheels, self.color)

# Использование:
builder = CarBuilder()
car = builder.set_engine("V8").set_color("red").build()
print(car.color)


from pydantic import BaseModel, Field, EmailStr, ConfigDict
from tools.fakers import fake

class UserSchema(BaseModel):
    """
    Description of the user structure.
    """
    model_config = ConfigDict(populate_by_name=True) # позволяет передавать как camelCase, так и snake_case без ошибок.

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class GetUserResponseSchema(BaseModel):
    """
    Description of the structure of the user creation response.
    """
    user: UserSchema

class UpdateUserRequestSchema(BaseModel):
    """
    Structure of the request to update a user.
    """
    model_config = ConfigDict(populate_by_name=True)

    # Добавили генерацию случайного email
    email: EmailStr | None = Field(default_factory=fake.email)
    # Добавили генерацию случайной фамилии
    last_name: str | None = Field(alias="lastName", default_factory=fake.last_name)
    # Добавили генерацию случайного имени
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)
    # Добавили генерацию случайного отчества
    middle_name: str | None = Field(alias="middleName", default_factory=fake.middle_name)

class UpdateUserResponseSchema(BaseModel):
    """
    Description of the structure of the user updating response.
    """
    user: UserSchema


class CreateUserResponseSchema(BaseModel):
    """
    Description of the structure of the user creation response.
    """
    user: UserSchema

class CreateUserRequestSchema(BaseModel):
    """
    Structure of the request to add a user.
    """
    model_config = ConfigDict(populate_by_name=True)

    # Добавили генерацию случайного email
    email: EmailStr = Field(default_factory=fake.email)
    # Добавили генерацию случайного пароля
    password: str = Field(default_factory=fake.password)
    # Добавили генерацию случайной фамилии
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    # Добавили генерацию случайного имени
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    # Добавили генерацию случайного отчества
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)
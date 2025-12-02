from pydantic import BaseModel, Field, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel

class UserSchema(BaseModel):
    """
    Description of the user structure.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    # in case when you need full name
    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CreateUserRequestSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    """
    Structure of the request to add a user.
    """
    email: EmailStr
    password: str
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """
    Description of the structure of the user creation response.
    """
    User: UserSchema


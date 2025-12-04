from pydantic import BaseModel, Field, EmailStr, ConfigDict

class UserSchema(BaseModel):
    """
    Description of the user structure.
    """
    model_config = ConfigDict(populate_by_name=True) #

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

    email: EmailStr = None
    last_name: str = Field(alias="lastName", default=None)
    first_name: str = Field(alias="firstName", default=None)
    middle_name: str = Field(alias="middleName", default=None)

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

    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
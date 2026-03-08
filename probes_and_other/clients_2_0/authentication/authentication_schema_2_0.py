from pydantic import BaseModel, Field, EmailStr
from tools.fakers import fake

class TokenSchema(BaseModel):
    """
    Description of the structure of authentication tokens. (using for LoginResponseDict)
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginRequestSchema(BaseModel):
    """TypedDict for login_api"""
    email: str = Field(default_factory=fake.email)  # Добавили генерацию случайного email
    password: str = Field(default_factory=fake.password)  # Добавили генерацию случайного пароля

class RefreshTokenRequestSchema(BaseModel):
    """TypedDict for refresh_token_api"""
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)

class LoginResponseSchema(BaseModel):
    """TypedDict for login response"""
    token: TokenSchema



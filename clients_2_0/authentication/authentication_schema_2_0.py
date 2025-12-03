from pydantic import BaseModel, Field, EmailStr

class TokenSchema(BaseModel):
    """
    Description of the structure of authentication tokens. (using for LoginResponseDict)
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginRequestSchema(BaseModel):
    """TypedDict for login_api"""
    email: EmailStr
    password: str

class RefreshTokenRequestSchema(BaseModel):
    """TypedDict for refresh_token_api"""
    refresh_token: str = Field(alias="refreshToken")

class LoginResponseSchema(BaseModel):
    """TypedDict for login response"""
    token: TokenSchema



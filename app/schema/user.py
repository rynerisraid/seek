from fastapi import status
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
class UserCreate(BaseModel):
    username: str
    email: str
    password: str  # 仅在创建时使用
    role: str = "member"

class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    created_at: datetime
    updated_at: datetime
    

class SignInRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class PasswordResetRequest(BaseModel):
    email: str
    new_password: str
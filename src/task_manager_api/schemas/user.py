# src/task_manager_api/schemas/user.py
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class UserRead(BaseModel):
    user_id: int
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

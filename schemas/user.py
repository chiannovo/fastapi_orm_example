'''
Author: ChiaEnKang
Date: 2025-06-11 02:30:37
LastEditors: ChiaEnKang
LastEditTime: 2025-06-11 02:57:18
'''
from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

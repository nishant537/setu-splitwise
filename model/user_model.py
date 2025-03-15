from typing import List
from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    username: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
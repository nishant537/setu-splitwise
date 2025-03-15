from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class GroupBase(BaseModel):
    name: str
    active: int = 1

class GroupCreate(GroupBase):
    pass

class GroupResponse(GroupBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class UserGroupBase(BaseModel):
    user_id: int
    group_id: int

class UserGroupCreate(UserGroupBase):
    pass

class UserGroupResponse(UserGroupBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True           
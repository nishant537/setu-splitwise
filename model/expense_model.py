from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from enum import Enum

class SplitType(str, Enum):
    equal = "equal"
    percentage = "percentage"
    manual = "manual"

class PaymentStatus(str, Enum):
    complete = "complete"
    pending = "pending"


class ExpenseBase(BaseModel):
    amount: float
    split_type: SplitType = SplitType.manual
    payment_status: PaymentStatus = PaymentStatus.pending

class ExpenseCreate(ExpenseBase):
    payee_id: int
    group_id: Optional[int]

class ExpenseResponse(ExpenseBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class UserExpenseBase(BaseModel):
    amount: float
    payment_status: str

class UserExpenseCreate(UserExpenseBase):
    expense_id: int
    user_id: Optional[int]
    group_id: Optional[int]

class UserExpenseResponse(UserExpenseBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True        

class PayExpenseResponse(BaseModel):
    user_id: int
    expense_id: int

    class Config:
        orm_mode = True        


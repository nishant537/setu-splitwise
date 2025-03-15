import random
import string
from db.database import *
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends,Header,Request,status,HTTPException
from typing import Optional, Union


async def get_all_users(db: Session):
    db_object = db.query(User).all()
    return db_object

async def create_user(db: Session, body):
    db_item = User(**body.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

async def get_user_balance(db: Session,user_id):
    credit_object = db.query(Expense).filter(Expense.payee_id == user_id).all()
    credit = 0
    for item in credit_object:
        credit+=item.amount
    
    debit_object = db.query(UserExpense).filter(UserExpense.user_id == user_id).all()
    debit = 0
    for item in debit_object:
        debit+=item.amount

    return credit - debit
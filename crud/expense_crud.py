import random
import string
from db.database import *
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends,Header,Request,status,HTTPException
from typing import Optional, Union
from crud.group_crud import get_group_users


async def get_all_expense(db: Session):
    db_object = db.query(Expense).all()
    return db_object

async def create_expense(db: Session, body):
    db_item = Expense(**body.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# user expense assignment

async def get_all_user_expense(db: Session):
    db_object = db.query(UserExpense).all()
    return db_object

async def assign_user_expense(db: Session, body):
    db_item = UserExpense(**body.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

async def assign_group_expense(db: Session, body):
    if body.group_id:
        all_users = get_group_users(db, body.group_id)
        for user in all_users:
            db_item = UserExpense(**body.dict(),**{"user_id":user.id})
            db.add(db_item)
            db.commit()
            db.refresh(db_item)
            return db_item
    else:
        raise HTTPException(status_code=404, detail="Group not found")

async def pay_user_expense(db: Session, body):
    db_item = db.query(UserExpense).filter(UserExpense.expense_id == body.expense_id, UserExpense.user_id == body.user_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Expense not found")
    db_item.payment_status = "Complete"
    db.commit()
    db.refresh(db_item)
    return db_item
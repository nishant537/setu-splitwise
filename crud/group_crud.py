import random
import string
from db.database import *
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends,Header,Request,status,HTTPException
from typing import Optional, Union


async def get_all_groups(db: Session):
    db_object = db.query(Group).all()
    return db_object

async def create_group(db: Session, body):
    db_item = Group(**body.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

async def assign_user_group(db: Session, body):
    db_item = UserGroup(**body.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

async def get_group_users(db: Session,group_id):
    db_object = db.query(Group).filter(Group.id == group_id).all()
    return db_object
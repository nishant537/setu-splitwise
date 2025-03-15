from enum import Enum as EnumClass
from databases import Database
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.types import JSON
from datetime import datetime

DATABASE_URL = 'sqlite:///./app.db'

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    active = Column(Boolean, default=True)

class UserGroup(Base):
    __tablename__ = 'user_groups'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    group_id = Column(Integer, ForeignKey('groups.id'))
    created_at = Column(DateTime, default=datetime.utcnow)    

class SplitType(EnumClass):
    equal = "equal"
    percentage = "percentage"
    manual = "manual"

class PaymentStatus(EnumClass):
    complete = "complete"
    pending = "pending"

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=True)
    payee_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float, nullable=False)
    split_type = Column(Enum(SplitType), nullable=False, default = SplitType.manual)
    payment_status = Column(Enum(PaymentStatus), nullable=False, default = PaymentStatus.pending)
    created_at = Column(DateTime, default=datetime.utcnow)

class UserExpense(Base):
    __tablename__ = 'user_expenses'
    id = Column(Integer, primary_key=True, index=True)
    expense_id = Column(Integer, ForeignKey('expenses.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float, nullable=False)
    payment_status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)    

Base.metadata.create_all(engine)
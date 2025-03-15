from fastapi import APIRouter, Depends
from fastapi.security.api_key import APIKeyHeader
# import auth
# from crud.dentalstall_crud import scrape_data
from sqlalchemy.orm import Session
from model.expense_model import *
from db.database import *
from crud.expense_crud import *

router = APIRouter(
    dependencies=[Depends(APIKeyHeader(name="token"))],
)

@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    return await get_all_expense(db)


@router.post('/',response_model=ExpenseResponse,)
async def create(body:ExpenseCreate, db: Session = Depends(get_db), ):
    return await create_expense(db,body)

@router.get('/assigned_expenses')
async def get_all(db: Session = Depends(get_db)):
    return await get_all_user_expense(db)

@router.post('/assign_user',response_model=UserExpenseResponse,)
async def assign_expense(body:UserExpenseCreate, db: Session = Depends(get_db), ):
    return await assign_user_expense(db,body)

@router.post('/assign_group',response_model=UserExpenseResponse,)
async def assign_group(body:UserExpenseCreate, db: Session = Depends(get_db), ):
    return await assign_group_expense(db,body)

@router.patch('/pay_expense',response_model=UserExpenseResponse,)
async def pay_expense(body:PayExpenseResponse, db: Session = Depends(get_db), ):
    return await pay_user_expense(db,body)




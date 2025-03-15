from fastapi import APIRouter, Depends
from fastapi.security.api_key import APIKeyHeader
# import auth
# from crud.dentalstall_crud import scrape_data
from sqlalchemy.orm import Session
from model.user_model import *
from db.database import *
from crud.user_crud import *

router = APIRouter(
    dependencies=[Depends(APIKeyHeader(name="token"))],
)

@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    return await get_all_users(db)

@router.post('/',response_model=UserResponse,)
async def create(body:UserCreate, db: Session = Depends(get_db), ):
    return await create_user(db,body)

@router.get('/get_balance/{user_id}')
async def get_balance(user_id:int,db: Session = Depends(get_db)):
    return await get_user_balance(db,user_id)
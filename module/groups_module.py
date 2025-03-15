from fastapi import APIRouter, Depends
from fastapi.security.api_key import APIKeyHeader
# import auth
# from crud.dentalstall_crud import scrape_data
from sqlalchemy.orm import Session
from model.group_model import *
from model.user_model import *
from db.database import *
from crud.group_crud import *

router = APIRouter(
    dependencies=[Depends(APIKeyHeader(name="token"))],
)

@router.get('/')
async def get_all(db: Session = Depends(get_db)):
    return await get_all_groups(db)

@router.post('/',response_model=GroupResponse,)
async def create(body:GroupCreate, db: Session = Depends(get_db), ):
    return await create_group(db,body)

@router.post('/assign_user',response_model=UserResponse,)
async def assign_expense(body:UserGroupCreate, db: Session = Depends(get_db), ):
    return await assign_user_group(db,body)

@router.get('/get_users/{group_id}',response_model=UserResponse,)
async def create(group_id:int, db: Session = Depends(get_db), ):
    return await get_group_users(db,group_id)

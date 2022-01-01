from typing import List
from fastapi import APIRouter, Depends
from schemas import UserBase, UserDispaly
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix='/users',
    tags=['user']
)

@router.post('/',response_model=UserDispaly)
def create_user(request:UserBase,db:Session=Depends(get_db)):
    return db_user.create_user(db,request)

@router.get('/',response_model=List[UserDispaly])
def get_users(db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.get_all_users(db)

@router.get('/{id}',response_model=UserDispaly)
def get_user(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.get_user(db,id)

@router.put('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.update_user(db,id,request)

@router.delete('/delete/{id}')
def delete_user(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.delete_user(db,id)
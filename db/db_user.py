
from sqlalchemy.orm.session import Session
from db.hash import Hash
from schemas import UserBase
from db.models import DbUser

def create_user(db:Session, request:UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash(request.password)
        
    )
    db.add(new_user)
    db.commmit()
    db.refresh(new_user)
    return new_user
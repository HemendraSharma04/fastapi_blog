from pydantic import BaseModel

class UserBase(BaseModel):
    username : str
    email : str
    password: str
    
class UserDispaly(BaseModel):
    username:str
    email:str
    class Config():
        orm_mode=True
    
        
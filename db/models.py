
from sqlalchemy.orm import column_property, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Integer,String
from sqlalchemy import Column
from db.database import Base

class DbUser(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String)
    email=Column(String)
    password=Column(String)
    items=relationship('DbArtile',back_populates='user')
    
class DbArticle(Base):
    __tablename__='artiles'
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    content=Column(String)
    published=Column(Boolean)
    user_id=Column(Integer,ForeignKey('users.id'))
    user = relationship("DbUser",back_populates='items')
    
    
    
    
    
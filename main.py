from fastapi import FastAPI
from router import blog_get
from router import blog_post
from router import user
from db import models
from db.database import engine

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)

@app.get('/hello')
def index():
  return {'message': 'Hello world!'}


models.Base.metadata.create_all(engine)
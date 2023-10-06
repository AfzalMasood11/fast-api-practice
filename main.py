from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Afzal'}}

@app.get('/about')
def about():
    return {'data': "It's about response"}

@app.get('/blogs/{id}/comments')
def blog_comments(id, limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if(published):
        return {'data': f'{limit} published blogs of {id} {sort}'}
    else:
        return {'data': f'{limit} blogs of {id} {sort}'}

# Its Pydentic who is managing the different datatypes, as shown below:
@app.get('/blogs/{id}')
def show(id: int):
    # get blog on the base of id = id.
    return {'data': id}

# For creating blog, you need to import BaseModel from pydentic and
# create a class, as shown blow:
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog has been created with title: {blog.title}'}


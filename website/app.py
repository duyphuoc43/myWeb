# myapp/app.py
from fastapi import FastAPI
from .schemas import Item

app = FastAPI()


@app.get("/")
async def read_root():
    '''Get'''
    return {"message": "Hello, World"}


@app.get("/items/")
async def read_root2():
    '''Get items'''
    return {"message": "Hello, Phuoc"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    '''Get items'''
    return {"item_id": item_id, "q": q}


@app.post("/items/")
async def create_item(request: Item):
    '''Post items'''
    return request

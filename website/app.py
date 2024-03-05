# myapp/app.py
from fastapi import FastAPI
from .schemas import Item,hourAndFlow,Image,Arrays
from .phuoc import predictions,coverData


app = FastAPI()

@app.get("/prediction/{flow}/{pressure}")
async def prediction_get(flow: float,pressure: float):
    '''Get prediction'''
    response = predictions(coverData(flow,pressure))
    return response

@app.post("/prediction/")
async def prediction(request: hourAndFlow):
    '''Post prediction'''
    response = predictions(coverData(request.flow,request.pressure))
    return response

@app.post("/array/")
async def prediction(request: Arrays):
    '''Post prediction'''
    response = predictions(request.array)
    return response

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
async def create_item(request: Item) -> Item:
    '''Post items'''
    return 



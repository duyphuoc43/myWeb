# myapp/app.py
from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

from .database import crud, models
from .schemas import Item, hourAndFlow, Image, Arrays, Statistics
from .phuoc import predictions, coverData

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import schemas
from .database import schemas as schemas_db
from .database.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/statistics/")
async def create_statistics(request: Statistics):
    return crud.create_statistics(request.date, request.flow, request.pressure)


@app.get("/users/", response_model=list[schemas_db.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/prediction/{flow}/{pressure}")
async def prediction_get(flow: float, pressure: float):
    '''Get prediction'''
    response = predictions(coverData(flow, pressure))
    return response


@app.post("/prediction/")
async def prediction(request: hourAndFlow):
    '''Post prediction'''
    response = predictions(coverData(request.flow, request.pressure))
    return response


@app.post("/upload_file/")
async def upload_image(file: UploadFile = File(...)):
    # Đảm bảo file là file ảnh
    if file.content_type.startswith('image'):
        contents = await file.read()
        with open("anhtest.png", "wb") as f:
            f.write(contents)


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

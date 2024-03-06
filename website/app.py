# myapp/app.py
from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

from .sql import crud, models
from .phuoc import predictions, coverData

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import schemas
from .sql.database import SessionLocal, engine

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
async def statistics(request: schemas.Statistics, db: Session = Depends(get_db)):
    return crud.create_statistics(db=db, request=request)


@app.get("/prediction/{flow}/{pressure}")
async def prediction_get(flow: float, pressure: float):
    '''Get prediction'''
    response = predictions(coverData(flow, pressure))
    return response


@app.post("/prediction/")
async def prediction(request: schemas.hourAndFlow):
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


@app.get("/")
async def read_root():
    '''Get'''
    return {"message": "Hello, World"}

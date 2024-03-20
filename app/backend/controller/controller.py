# myapp/app.py

from fastapi import FastAPI, File, UploadFile
from typing import Annotated
from ..schemas import Item, hourAndFlow, Arrays, Image, Statistics, History
from ..service import coverData, predictions, add_data, get_data, add_history, get_history
from fastapi import FastAPI, File, UploadFile
from typing import Union


app = FastAPI()


@app.get("/")
async def read_root():
    '''Get'''
    return {"message": "Hello, World"}


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


@app.post("/upload-file/")
async def upload_image(file: UploadFile = File(...)):
    # Đảm bảo file là file ảnh
    if file.content_type.startswith('image'):
        contents = await file.read()
        with open("anhtest.png", "wb") as f:
            f.write(contents)


@app.post("/post-data/")
async def post_data(request: Statistics):
    '''Post data'''
    add_data(request)
    return "Đã Cập Nhập"


@app.get("/get-data/")
async def get_dat():
    '''Get data'''
    response = get_data()
    return response


@app.post("/post-history/")
async def post_data(request: History):
    '''Post History'''
    add_history(request)
    return "Đã Cập Nhập"


@app.get("/get-history/{date}")
async def get_dat(date: str):
    '''Get data'''
    response = get_history(date)
    return response

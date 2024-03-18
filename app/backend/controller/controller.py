# myapp/app.py

from fastapi import FastAPI, File, UploadFile
from typing import Annotated
from ..schemas import Item, hourAndFlow, Arrays, Image, Statistics
from ..service import coverData, predictions, add_values_to_last_row, add_data
from fastapi import FastAPI, File, UploadFile
from typing import Union
import uvicorn

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


@app.post("/upload_file/")
async def upload_image(file: UploadFile = File(...)):
    # Đảm bảo file là file ảnh
    if file.content_type.startswith('image'):
        contents = await file.read()
        with open("anhtest.png", "wb") as f:
            f.write(contents)


@app.get("/get-data/")
async def get_data():
    response = add_data()
    return response

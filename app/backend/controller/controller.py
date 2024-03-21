# myapp/app.py

from fastapi import FastAPI, File, UploadFile
from typing import Annotated
from ..schemas import Item, hourAndFlow, Arrays, Image, Statistics, History,HistoryDate
from ..service import coverData, predictions, add_data, get_data, add_history, get_history
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from typing import Union
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    '''Get'''
    response = {"message": "Hello, World"}
    return JSONResponse(content=response)


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
async def post_history(request: History):
    '''Post History'''
    add_history(request)
    return "Đã Cập Nhập"


@app.get("/get-history/{date}")
async def history(date: str):
    '''Get history'''
    response = get_history(date)
    return response

@app.post("/get-history/")
async def history(request : HistoryDate):
    '''Post history'''
    response = get_history(request.date)
    print(response)
    return response
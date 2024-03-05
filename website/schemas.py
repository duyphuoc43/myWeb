from pydantic import BaseModel
from typing import List


class Item(BaseModel):

    name: str
    description: str = None
    price: float = None
    tax: float = None


class hourAndFlow(BaseModel):
    pressure: float
    flow: float


class Arrays(BaseModel):
    array: List[float]


class Image(BaseModel):
    image: List[List[float]]


class Statistics(BaseModel):
    date: str
    flow: float
    pressure: float

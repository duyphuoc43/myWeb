from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    
    name: str
    description: str = None
    price: float = None
    tax: float = None


class hourAndFlow(BaseModel):
    pressure: float
    flow : float

class Arrays(BaseModel):
    array: List[float]

class Image(BaseModel):
    image: List[List[float]]


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True


from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str = None
    price: float = None
    tax: float = None

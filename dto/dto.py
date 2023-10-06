from pydantic import BaseModel

class Product(BaseModel):
    id: int
    title: str
    price: int
    timing: str
    owner: int
    img: str
    descr: str

class Basa(BaseModel):
    id: int
    bio: str
    date: str
    img: str
    descr: str
    client: bool
    implementer: bool
    listOfOrders: list
    listOfServices: list
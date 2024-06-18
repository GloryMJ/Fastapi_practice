# response model
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str = None
#     price: float
    
# def get_item_from_db(id):
#     return {
#         "name": "simple item",
#         "description": "A simple item description",
#         "price": 50.0,
#         "dis_price": 45.0
#     }

# @app.get("/items/{item_id}", response_model=Item)
# def read_item(item_id: int):
#     item = get_item_from_db(item_id)
#     return item

# ------

# pydantic with basic response model
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
    
# @app.get("/item/", response_model=Item)
# def get_item():
#     return {
#         "name": "milk",
#         "price": 3.5
#     }
#----------------

# Generic response model
# from typing import TypeVar, Generic
# from fastapi import FastAPI
# from pydantic.generics import GenericModel

# app = FastAPI()

# T = TypeVar("T")

# class GenericItem(GenericModel, Generic[T]):
#     data: T

# @app.get("/generic_item/", response_model=GenericItem[str])
# async def get_generic_item():
#     return {"data": "generic item"}
#-------------------------------

# Union response model
# from typing import Union
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Cat(BaseModel):
#     name: str

# class Dog(BaseModel):
#     name: str
    
# @app.get("/animal/", response_model=Union[Cat, Dog])
# async def get_animal(animal: str):
#     if animal  == 'cat':
#         return Cat(name="Whiskers")
#     else:
#         return Dog(name="Fido")
#----------------------------------

# List response model
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str

@app.get("/items/", response_model=List[Item])
async def get_items():
    return [{"name": "MJ"}, {"name": "Kobe"}]

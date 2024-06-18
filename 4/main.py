# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Image(BaseModel):
#     url: str
#     name: str

# class Item(BaseModel):
#     name: str
#     description: str
#     image: Image

# @app.post("/items/")
# def create_item(item: Item):
#     return {"item": item.dict()}
#5.5.3----------------

# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List, Union

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     tags: List[str]
#     variant: Union[int, str]

# @app.post("/items/")
# def create_item(item: Item):
#     return {"item": item.dict()}
#5.5.4-------------------------

# from typing import TypeVar, Generic
# from pydantic import BaseModel

# T = TypeVar('T')

# class GenericItem(BaseModel, Generic[T]):
#     name: str
#     content: T

# -------

from typing import TypeVar, Generic
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

T = TypeVar("T")

class GenericItem(BaseModel, Generic[T]):
    name: str
    content: T

@app.post("/generic_items/")
def create_item(item: GenericItem[int]):
    return {"item": item.dict()} 

#-----5.5.5
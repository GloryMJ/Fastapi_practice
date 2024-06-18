from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    # None 값 허용 즉 Null 허용 (Django)
    price: float
    is_offer: bool = None
    tax : float = 0.1

class Item2(BaseModel):
    name: str = Field(..., title="Item Name", min_length=2, max_length=50)
    # ..., ellipsis 필드가 필수임을 나타내는데 사용 버전에 따라 생략 가능
    description: str = Field(None, description="The description of the item", max_length=300)
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tag: List[str] = Field(default=[], alias="item-tags")

@app.post("/items/")
def create_item(item: Item):
    return {"item": item.dict()}

@app.post("/items2/")
async def create_item(item: Item2):
    return {"item": item.dict()}
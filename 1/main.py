from fastapi import FastAPI, Query
from typing import List, Dict

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, MJ"}

# @app.get("/items/{item_id}")
# def read_item(item_id):
#     return {"item_id": item_id}

@app.get("/users/{user_id}/items/{item_name}")
def read_user_item(user_id, item_name):
    return {"user_id": user_id, "item_name": item_name}

# 디폴트 값 미설정
# @app.get("/items/")
# def read_items(skip, limit):
#     return {"skip": skip, "limit": limit}

# 디폴트 값 설정
@app.get("/items/")
def read_items(skip = 0, limit = 10):
    return {"skip": skip, "limit": limit}

#------------------------------------------

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/getdata/")
def read_items(data: str = "MJ"):
    return {"data" : data}

#-----------------------------------------

@app.get("/primaryitems/")
def read_items(q: List[int] = Query([])):
    return {"q": q}

@app.post("/create/")
def create_item(item: Dict[str, int]):
    return item
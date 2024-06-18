# request
# query parameter + request body / ? key=value
from fastapi import FastAPI, Query, Body

app = FastAPI()

@app.get("/users/")
def read_users(q: str = Query(None, max_length=50, deprecated=True)):
    # null 값 허용 및 최대 길이 50
    # q 사용하지 말 것 -> deprecated 사용으로 쿼리문 교체
    return {"Q": q}
    # JSON 객체 반환
    
# @app.get("/items/")
# def read_items(internal_query: str = Query(None, alias="search")):
#     return {"query_handled": internal_query}
    # alias 썼다면 query문 또한 alias 따를 것
    
@app.get("/info/")
def read_info(info: str = Query(None, description="정보를 입력하세요")):
    return {"info": info}

@app.get("/items/")
def read_items(item_id: int = Query(...)):
    return {"item_id": item_id}

@app.post("/items/")
def create_item(item: dict = Body(...)):
    return {"item": item}

@app.post("/advanced_items/")
def create_advanced_item(
    item: dict = Body(
        default=None,
        example={"key":"value"},
        media_type="application/json",
        alias="item_alias",
        title="Sample",
        description="This is a sample",
        deprecated=False
    )
):
    return {"item": item}
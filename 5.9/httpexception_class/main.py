from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id == 42:
        raise HTTPException(status_code=404, detail="관리자 페이지 입니다", headers={"X-Error": "There was an error"})
    return {"item_id": item_id}

# raise HTTPException(
#     status_code=401,
#     detail= "Not Auth",
#     headers={"WWW-Authenticate": "Bearer"}
# )

# raise HTTPException(
#     status_code=429,
#     detail="Too Many",
#     headers={"Retry-After": "120"}
# )

# raise HTTPException(
#     status_code=429,
#     detail="Rate limit exceeded",
#     headers={"X-Rate-Limit": "100"}
# )

# raise HTTPException(
#     status_code=500,
#     detail="Internal Server Error",
#     headers={"X-Error": "Database connection failed"}
# )

# raise HTTPException(
#     status_code=200,
#     detail="Response Information",
#     headers={"Cache-Control": "no-cache"}
# )

# raise HTTPException(
#     status_code=201,
#     detail="New item created",
#     headers={"Location": "/items/5"}
# )

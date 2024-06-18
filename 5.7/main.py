# response class
from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse, PlainTextResponse, RedirectResponse

app = FastAPI()

@app.get("/json", response_class=JSONResponse)
def read_json():
    return {"msg": "JSON"}

@app.get("/html", response_class=HTMLResponse)
def read_html():
    return "<h1> HTML <h1>"

@app.get("/redirect")
def read_redirect():
    return RedirectResponse(url="/text")
# django 생각하면 redirect 구문일거고

@app.get("/text", response_class=PlainTextResponse)
def read_text():
    return "Text"



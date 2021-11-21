#imports
from os import name
from typing import Optional
from fastapi import FastAPI, Request

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")

app = FastAPI()
# Official Documentation : https://fastapi.tiangolo.com/tutorial/

app.mount("/static", StaticFiles(directory="static"),name="static")

# routes{------------------------------------------------------------

# When building APIs, you normally use these specific HTTP methods to perform a specific action.
# Normally you use:
# POST: to create data.
# GET: to read data.
# PUT: to update data.
# DELETE: to delete data.
# So, in OpenAPI, each of the HTTP methods is called an "operation".

# path operation decorator
@app.get("/")
def root_api():
    # You can return a dict, list, singular values as str, int, etc.
    # You can also return Pydantic models 
    return { "msg" : "FastAPI home template"}


# Basic application created can check by running command:>uvicorn main:server --reload 
# OpenAPI/ Swaggers at > http://127.0.0.1:8000/docs
# > http://127.0.0.1:8000/redoc

# raw OpenAPI schema looks like, FastAPI automatically generates a JSON (schema) with the descriptions of all your API.
# You can see it directly at: http://127.0.0.1:8000/openapi.json


@app.get("/home", response_class= HTMLResponse)
def home(request : Request):
    return templates.TemplateResponse("home.html", 
                                      { "request" : request, "title" : "Home Page", "text" : "This is FastAPI template"}
                                      )


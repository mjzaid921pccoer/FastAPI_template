#imports
from typing import Optional
from fastapi import FastAPI, Request
from fastapi import responses

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

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
    # return { "msg" : "FastAPI home template"} # v2.0
    return RedirectResponse(url="/app")
    


# Basic application created can check by running command:>uvicorn main:server --reload 
# OpenAPI/ Swaggers at > http://127.0.0.1:8000/docs
# > http://127.0.0.1:8000/redoc

# raw OpenAPI schema looks like, FastAPI automatically generates a JSON (schema) with the descriptions of all your API.
# You can see it directly at: http://127.0.0.1:8000/openapi.json


@app.get("/home", response_class= HTMLResponse)
def home(request : Request):
    response = { "request" : request, "title" : "Home Page", "text" : "This is FastAPI template"}
    return templates.TemplateResponse("home.html", response )

@app.get("/app", response_class= HTMLResponse)
def home(request : Request):
    
    intro = "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. The key features are: Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available."
    # list (iterable)
    features = [ "open standards : OpenAPI for API creation, including declarations of path operations, parameters, body requests, security, etc.",
                 "open standards : Automatic data model documentation with JSON Schema (as OpenAPI itself is based on JSON Schema).",
                 "open standards : Designed around these standards, after a meticulous study. Instead of an afterthought layer on top.",
                 "open standards : This also allows using automatic client code generation in many languages.",
                 "Automatic docs : Swagger UI, with interactive exploration, call and test your API directly from the browser.",
                 "Automatic docs : Alternative API documentation with ReDoc.",
                 "Just Modern Python It's all based on standard Python 3.6 type declarations (thanks to Pydantic). No new syntax to learn. Just standard modern Python. If you need a 2 minute refresher of how to use Python types (even if you don't use FastAPI), check the short tutorial: Python Types.",
                 "Security and authentication Security and authentication integrated. Without any compromise with databases or data models.",
                 "Dependency Injection FastAPI includes an extremely easy to use, but extremely powerful Dependency Injection system.",
                 "Unlimited 'plug-ins'",
                 "Tested 100% test coverage. 100% type annotated code base. Used in production applications.",
                 "Starlette features FastAPI is fully compatible with (and based on) Starlette. So, any additional Starlette code you have, will also work. FastAPI is actually a sub-class of Starlette. So, if you already know or use Starlette, most of the functionality will work the same way. With FastAPI you get all of Starlette's features (as FastAPI is just Starlette on steroids)"
                ]
    # dict
    creator = { "name" : "Sebastián Ramírez", "LinkedIn" : "https://www.linkedin.com/in/tiangolo/"}
    response = { "request" : request, "title" : "App", "introduction" : intro, "Features" : features, "creator" : creator}
    return templates.TemplateResponse("index.html", response)

@app.get("/id")
def read_item(q: Optional[str] = None):
    if q:
        return {"q": q}
    return {"No Query": ""}

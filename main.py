#imports
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root_api():
    return { "msg" : "FastAPI home template"}

@app.get("/{id}")
def apiId(id : int, q : Optional[str] = None):
    return {"id": id, "Query": q}
from fastapi import FastAPI, File, UploadFile, Form, Body
# from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

@app.post("/upload-form/")
async def upload_form(name: str = Form(...), email: str = Form(...)):
    return {"name": name, "email": email}

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float

@app.post("/mixed-data/")
async def mixed_data(
    item: str = Form(...),
    file: UploadFile = File(...),
    comment: str = Form(...)
):
    item_obj = Item(**json.loads(item))
    return {
        "item_name": item_obj.name,
        "file_name": file.filename,
        "comment": comment
    }

@app.post("/json-data/")
async def json_data(item: Item):
    return item

@app.post("/multiple-files/")
async def multiple_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}
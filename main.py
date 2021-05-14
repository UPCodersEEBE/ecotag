from typing import Optional

from fastapi import FastAPI

app = FastAPI()

from pymongo import MongoClient

alex=MongoClient('mongodb+srv://tampier:tampier@cluster0.wybmf.mongodb.net/ecotag?retryWrites=true&w=majority')
db = alex['ecotag']
collection = db['object']

@app.get("/")
def read_root():
    collection.insert_one({"Hello":"World"})
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
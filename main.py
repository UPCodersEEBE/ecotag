from typing import Optional, Any, Dict

from fastapi import FastAPI, Request

app = FastAPI()

from process_typeform import get_object_from_quest

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



@app.post("/object")
def create_object(request: Dict[Any, Any]):
    object=get_object_from_quest(request)
    collection.insert_one(object)
    return object

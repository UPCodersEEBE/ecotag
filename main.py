from threading import Event
from typing import Optional, Any, Dict

from fastapi import FastAPI, Request

app = FastAPI()

from process_typeform import get_object_from_quest, get_event_from_quest
from event_to_object_connection import update_event_from_object

from pymongo import MongoClient

import json

alex=MongoClient('mongodb+srv://tampier:tampier@cluster0.wybmf.mongodb.net/ecotag?retryWrites=true&w=majority')
db = alex['ecotag']
object_collection = db['objects']
event_collection = db['events']

@app.get("/")
def read_root():
    object_collection.insert_one({"Hello":"World"})
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}



@app.post("/create_object")
def create_object(request: Dict[Any, Any]):
    object=get_object_from_quest(request)
    object_collection.insert_one(object)
    return object


@app.post("/create_event")
def create_event(request: Dict[Any, Any]):
    event=get_event_from_quest(request)
    print(event)
    event_collection.insert_one(event)
    print("line 44")
    update_event_from_object(event)
    return event
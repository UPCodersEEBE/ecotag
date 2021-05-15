from queries_mongo import get_impact_from_obj
from threading import Event
from typing import Optional, Any, Dict

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


from process_typeform import get_object_from_quest, get_event_from_quest
from event_to_object_connection import update_event_from_object
from qr_processing import normal_qr
from qr_processing import qr_colors

from environmental_impact import get_grade_from_impact

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


@app.post("/create_object")
def create_object(request: Dict[Any, Any]):
    object=get_object_from_quest(request)
    object_collection.insert_one(object)
    return object


@app.post("/create_event")
def create_event(request: Dict[Any, Any]):
    event=get_event_from_quest(request)
    event_collection.insert_one(event)
    update_event_from_object(event)
    return event

@app.get("/last_object", response_class=HTMLResponse)
async def last_object(request: Request):
    object = object_collection.find().limit(1).sort([('$natural',-1)])
    id=str(list(object)[0]["_id"])
    qr=normal_qr(id)
    return templates.TemplateResponse("items.html", {"request": request, "id":id})

@app.get("/qr_coloraines/{id}")
async def qr_coloraines(request: Request, id:str):
    impact=get_impact_from_obj(id)
    grade=get_grade_from_impact(impact)
    qr=qr_colors(id, grade)
    return templates.TemplateResponse("items.html", {"request": request, "id":id})
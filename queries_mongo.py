import pymongo

client = pymongo.MongoClient("mongodb+srv://tampier:tampier@cluster0.wybmf.mongodb.net/ecotag?retryWrites=true&w=majority")

db = client.ecotag

objects = db.objects

def get_events_id_from_obj(object_id):
    object=objects.find_one({"_id": object_id})
    events = object["events"]
    if events==None:
        events=[]
    return events

def get_impact_from_obj(object_id):
    object=objects.find_one({"_id": object_id})
    try:
        impact = object["impact"]
    except:
        impact={}
    return impact


    

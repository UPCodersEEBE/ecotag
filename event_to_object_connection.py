
from queries_mongo import get_events_id_from_obj,get_impact_from_obj
from pymongo import MongoClient

alex=MongoClient('mongodb+srv://tampier:tampier@cluster0.wybmf.mongodb.net/ecotag?retryWrites=true&w=majority')
db = alex['ecotag']
object_collection = db['objects']
event_collection = db['events']

def update_event_from_object(event): 
    
    event_id = { "_id": event["_id"] }
    object_id= event["object"]
    query={"_id":object_id}

    prev_impact= get_impact_from_obj(object_id)
    print(prev_impact)
    new_impact= event["impact"]
    for k in new_impact.keys():
        if k not in prev_impact.keys():
            prev_impact[k]=0
        prev_impact[k]+=new_impact[k]
    newvalues = { "$set": { "impact": prev_impact } }
    
    list_of_events=get_events_id_from_obj(object_id)
    print (list_of_events)
    list_of_events.append(event_id)
    print (list_of_events)

    newvalues = { "$set": { "impact": prev_impact , "events": list_of_events} }

    object_collection.update_one(query, newvalues)

    
    return prev_impact
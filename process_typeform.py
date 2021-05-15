import uuid

from queries_mongo import get_number_of_events_from_obj


def get_object_from_quest (dict):
    object_id = str(uuid.uuid4())
    form_response=dict["form_response"]
    answers=form_response["answers"]
    
    description = answers[0]["text"]
    if answers[1]["boolean"]:
        predecessors = answers[2]["text"]
        predecessors = list(predecessors)
    else:
        predecessors = []

    object_info = {
        "_id":object_id,
        "description" :description,
        "predecessors":predecessors,
        "events":[]
        
    }

    return object_info

def get_event_from_quest(dict):

    form_response=dict["form_response"]
    answers=form_response["answers"]
    
    object_id = answers[0]["text"]
    n=get_number_of_events_from_obj(object_id)
    event_id=object_id+"_"+str(n)

    description = answers[1]["text"]
    CO2 = answers[2]["number"]
    H2O = answers[3]["number"]
    kWh = answers[4]["number"]
    impact={"CO2":CO2,"H2O":H2O,"E":kWh}

    event_info = {
        "_id":event_id,
        "object": object_id,
        "description":description,
        "impact":impact
    }
    
    return event_info



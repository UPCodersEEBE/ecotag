import uuid

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
        "predecessors":predecessors
    }

    return object_info

def get_event_from_quest(dict):


import uuid

from queries_mongo import get_events_id_from_obj, get_impact_from_obj

from functions_for_process_typeform import get_predecessors_environmental_impact,get_fraction_from_predecessors, get_environmental_impact_right

def get_object_from_quest (quest):
    object_id = str(uuid.uuid4())[0:12]
    form_response=quest["form_response"]
    answers=form_response["answers"]
    
    description = answers[0]["text"]

    if answers[3]["boolean"]: #sihi ha predeessors agafa el seu imacte
        predecessors = from_string_to_list(answers[5]["text"])
        fraction_predecessors = from_string_to_list(answers[6]["text"])

        environmental_impact_pred = get_predecessors_environmental_impact(predecessors)  #sumat
        fraction_predecessors = get_fraction_from_predecessors(fraction_predecessors)    

        environmental_impact = get_environmental_impact_right(predecessors, fraction_predecessors)

    else:
        predecessors = []
        environmental_impact={}
        fraction_predecessors = []

    category = answers[1]["choice"]
    weight = answers[2]["number"]
    recycled = answers[3]["boolean"]

    predecessor_dict = dict(zip(predecessors, fraction_predecessors))
    impact_weight = {}
    for key in environmental_impact.keys():
        impact_weight[key]=environmental_impact[key]*weight/1000
    
    object_info = {
        "_id":object_id,
        "description" :description,
        "predecessors":predecessor_dict,
        "events":[],
        "impact":environmental_impact,
        "impact_weight": impact_weight,
        "category":category,
        "weight": weight,
        "recycled": recycled,
    }

    return object_info

def get_event_from_quest(dict):

    form_response=dict["form_response"]
    answers=form_response["answers"]
    
    object_id = answers[0]["text"]

    n=len(get_events_id_from_obj(object_id))
    
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


def from_string_to_list(stringa): #predecessors from string as answer on typeform to list
    if "," in stringa:
         l = list(f"[{stringa}]")
    else:
          l=[stringa]
    return l



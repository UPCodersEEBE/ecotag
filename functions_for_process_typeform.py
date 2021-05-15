from queries_mongo import get_impact_from_obj

def get_predecessors_environmental_impact(predecessors):
    if "," in predecessors:
         predecessors = list(f"[{predecessors}]")
    else:
          predecessors=[predecessors]
    environmental_impact={}
    for predecessor in predecessors:
        impact=get_impact_from_obj(predecessor)
        for key in impact:
            if key in environmental_impact.keys():
                environmental_impact[key] += impact[key]
            else:
                 environmental_impact[key] = impact[key]

    return environmental_impact

def get_fraction_from_predecessors(fraction_predecessors):
    if "," in fraction_predecessors:
         fraction_predecessors = list(f"[{fraction_predecessors}]")
    else:
          fraction_predecessors=[fraction_predecessors]
    return fraction_predecessors
    
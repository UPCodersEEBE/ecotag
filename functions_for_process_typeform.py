from queries_mongo import get_impact_from_obj

def get_predecessors_environmental_impact(predecessors):
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
    

def get_environmental_impact_right(predecessors,fraction_predecessors):
    list_of_env_imp=[]
    for predecessor in predecessors:
        list_of_env_imp.append(get_impact_from_obj(predecessor))

    print(list_of_env_imp)
    env_imp_right={}
    for key in list_of_env_imp[0].keys():
        print(key)
        sum=0
        for i in range(0,len(predecessors)):
            print(list_of_env_imp[i][key])
            print(fraction_predecessors[i])
            sum+=list_of_env_imp[i][key]*fraction_predecessors[i]
        env_imp_right[key]=sum

    return env_imp_right
        


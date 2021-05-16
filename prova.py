def get_environmental_impact_right(list_of_env_imp,fraction_predecessors):


    env_imp_right={}
    for key in list_of_env_imp[0].keys():
        sum=0
        for i in range(0,len(list_of_env_imp)):
            sum+=list_of_env_imp[i][key]*fraction_predecessors[i]
        env_imp_right[key]=sum

    return env_imp_right
        
list_of_env_imp=[{"CO2": 20, "H2O": 10, "kWh":13},{"CO2": 10, "H2O": 0, "kWh":343}]
fraction_predecessors=[0.1,0.9]
print(get_environmental_impact_right(list_of_env_imp,fraction_predecessors))
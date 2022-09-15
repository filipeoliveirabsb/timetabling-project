import numpy as np
import pandas as pd
import random
from ruamel.yaml import YAML

# *------------------ RULES ---------------------*
# the intervals between schedules are 3 days long
# optimal number of hours in month / agent=160h
# max hours in month / agent = 168h
# min agents / day in module = 2
# max agents / day in module = 4 (team lenght) 

# A solução deve:
# 1) gerar as escalas com o algoritmo heuristico 
#    com o arranjo de times (até 24).
#    Ex:
#       Escala1 => d1=t1, d2=t2, d3=t3, d4=t4
#       Escala2 => d1=t2, d2=t4, d3=t3, d4=t1
#       ...
# 2) na geração da escala, 
#    2.1) considerar as ausências de cada time e 
#           que há um time (4 agentes) por dia
#    2.2) gerar randomicamente pelos arranjos da 
#           ordem dos times    
# 3) somar as horas dos agentes no mês incluir na
#    coluna "total horas" no time_table
# 4) utilizar o algoritmo genetico pra encontrar a 
#    melhor escala, com setTime para medir o tempo 
#    de execução

def get_scale_constraints(team):
    
    constraints = data["scale_constraints"].index()

    print('test')

    return constraints

# generate time_table scale with heuristic algorithm
def get_time_tables(data, possibility):
    time_table = pd.DataFrame(index=data["agents"], columns=data["days"])

    modules = data["modules"]
    days = data["days"]
    agents = data["agents"]
    schedule = data["team_schedule"]

    shape = (len(modules) * len(days) * len(agents), len(schedule))
    genes = np.zeros(shape, dtype=np.int32)

    for j in range(len(possibility)):
        team = possibility[j]
        print(team)

        """ team_agents = schedule[j].index(team)
        print(team_agents) """

    for day in range(len(days)):
        
        for agent in range(len(agents)):
            
            for sch in range(len(schedule)):
                # indx = agent + day * len(agents) + module_name * len(days) * len(agents)
                # print(sch)

                (team, _, _) = schedule[sch]
                team_safe = 't1'
                if team == team_safe:
                    time_table.iloc[agent, day] = "X"

    return time_table        

if __name__ == '__main__':
    data_file = "./raw_data.yaml"
    raw_data_file = open(data_file)
    data = YAML().load(raw_data_file.read())
    raw_data_file.close()

    #print(data)
    possibilities = data["scale_possibilities"]


    for i in range(len(possibilities)):
        #for c in data["modules"]:
        #print("module : {}".format(c))
        print(i)
        print("------- Possibility -------")
        pos = possibilities[i]
        print(pos)
        print("---------------------------")
        print(get_time_tables(data, pos))


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
#    com o arranjo de times (até 18).
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

def get_employee_absences(team_agent):
    
    absences = data["scale_constraints"].index()

    return absences

# generate time_table scale with heuristic algorithm
def get_time_tables(data, poss):
    time_table = pd.DataFrame(index=data["agents"], columns=data["days"])

    modules = data["modules"]
    days = data["days"]
    agents = data["agents"]
    schedule = data["team_schedule"]
    
    #shape = (len(modules) * len(days) * len(agents), len(schedule))
    #genes = np.zeros(shape, dtype=np.int32)

    (first, second, third, fourth) = poss
        
    for k in range(len(schedule)):
    
        (team, team_agent, _) = schedule[k]

        if team == first:

            (scale_days) = data["scale_days"][0]

            create_scheduling(time_table, days, agents, team_agent, scale_days)

        if team == second:

            (scale_days) = data["scale_days"][1]

            create_scheduling(time_table, days, agents, team_agent, scale_days)

        if team == third:

            (scale_days) = data["scale_days"][2]

            create_scheduling(time_table, days, agents, team_agent, scale_days)                       
                    
        if team == fourth:

            (scale_days) = data["scale_days"][3]

            create_scheduling(time_table, days, agents, team_agent, scale_days) 

    return time_table



def create_scheduling(time_table, days, agents, team_agent, scale_days):
    for day in range(len(days)):
        for agent in range(len(agents)):
                    
            if (agents[agent] == team_agent and day in scale_days):
                
                # employee absences
                """ employee_absences = get_employee_absences(team_agent)
                for ab in range(len(employee_absences)):
                    (absences_type, absences_days) = employee_absences[ab]

                if day in range(absences_days):
                    time_table.iloc[agent, day] = absences_type  
                else: """
                time_table.iloc[agent, day] = 24


if __name__ == '__main__':
    data_file = "./raw_data.yaml"
    raw_data_file = open(data_file)
    data = YAML().load(raw_data_file.read())
    raw_data_file.close()

    #print(data)
    possibilities = data["order_possibilities"]
    last_schedule = data["last_schedule"]

    for i in range(len(possibilities)):
        #for c in data["modules"]:
        #print("module : {}".format(c))
        #print(i)
        #print("------- Possibility -------")
        
        poss = possibilities[i]

        #print(pos)
        #print("---------------------------")

        (first, _, _, _) = possibilities[i]
        (last_team) = last_schedule[0]

        #print(first)
        #print(last_team)
        # descarta que o último do mês anterior seja o primeiro do mês atual
        if last_team != first:
            print(get_time_tables(data, poss))
            print("fim")


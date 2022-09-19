import numpy as np
import pandas as pd
import random
from ruamel.yaml import YAML

# *------------------ RULES ---------------------*
# the intervals between schedules are 3 days long
# optimal number of hours in month / employee=160h
# max hours in month / employee = 168h
# min employees / day in module = 2
# max employees / day in module = 4 (team lenght) 

# A solução deve:
# 1) gerar as escalas com o algoritmo heuristico 
#    com o arranjo de times (até 18).
#    Ex:
#       Escala1 => d1=t1, d2=t2, d3=t3, d4=t4
#       Escala2 => d1=t2, d2=t4, d3=t3, d4=t1
#       ...
# 2) na geração da escala, 
#    2.1) considerar as ausências de cada time e 
#           que há um time (4 empregados) por dia
#    2.2) gerar randomicamente pelos arranjos da 
#           ordem dos times    
# 3) somar as horas dos empregados no mês incluir 
#    na coluna "total horas" no time_table
# 4) utilizar o algoritmo genetico pra encontrar a 
#    melhor escala, com setTime para medir o tempo 
#    de execução

def get_employee_absences(absences, team_employee, day):

    for ab in range(len(absences)):
        # employee, type of absence, days of absence
        (emp, toa, doa) = absences[ab]
        emp = emp['employee']
        toa = toa['type']
        doa = doa['days']

        if emp == team_employee:
            if day in doa:
                return (_, toa, _)
        
    return (_, 0, _)
        
        


# generate time_table scale with heuristic algorithm
def get_schedule_tables(data, poss, days, employees, schedule, absences):
    schedule_table = pd.DataFrame(index=data["employees"], columns=data["days"])

    (first, second, third, fourth) = poss
        
    for k in range(len(schedule)):
    
        (team, team_employee, _) = schedule[k]

        if team == first:

            (scale_days) = data["scale_days"][0]

            create_scheduling(schedule_table, days, employees, team_employee, scale_days, absences)

        if team == second:

            (scale_days) = data["scale_days"][1]

            create_scheduling(schedule_table, days, employees, team_employee, scale_days, absences)

        if team == third:

            (scale_days) = data["scale_days"][2]

            create_scheduling(schedule_table, days, employees, team_employee, scale_days, absences)                       
                    
        if team == fourth:

            (scale_days) = data["scale_days"][3]

            create_scheduling(schedule_table, days, employees, team_employee, scale_days, absences) 

    return schedule_table



def create_scheduling(schedule_table, days, employees, team_employee, scale_days, absences):
    for day in range(len(days)):
        for employee in range(len(employees)):
                   
            if (employees[employee] == team_employee and day in scale_days):
                
                # employee absences
                (_, toa, _) = get_employee_absences(absences, team_employee, day)
                
                #print(day)
                #print(doa)
                #print(emp)
                #print(team_employee)

                if (toa != 0):
                    schedule_table.iloc[employee, day] = toa
                else:
                    schedule_table.iloc[employee, day] = 24


if __name__ == '__main__':
    data_file = "./raw_data.yaml"
    raw_data_file = open(data_file)
    data = YAML().load(raw_data_file.read())
    raw_data_file.close()

    # copy the data
    possibilities = data["order_possibilities"]
    last_schedule = data["last_schedule"]
    days = data["days"]
    employees = data["employees"]
    schedule = data["team_schedule"]

    absences = data["month"]["jan"]["absences"]
    # (emp, type_abs, days_abs) = absences[0]

    #print(emp['employee'])
    #print(type_abs['type'])
    #print(days_abs['days'])

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

        # the last team can't be the first on this month
        if last_team != first:
            print(get_schedule_tables(data, poss, days, employees, schedule, absences))
            
    print("fim")


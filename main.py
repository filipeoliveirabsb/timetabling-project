import numpy as np
import pandas
import pandas as pd
from ruamel.yaml import YAML

# *------------------ RULES ---------------------*
# the intervals between schedules are 3 days long
# optimal number of hours in month / employee=160h
# max hours in month / employee = 168h
# min employees / day in module = 2
# max employees / day in module = 4 (team lenght) 

# The algorithm:
# 1) generate the scales with the heuristic algo-
#    rithm with the team arrangement (up to 18).
#    e.g:
#       scale1 => d1=t1, d2=t2, d3=t3, d4=t4
#       scale2 => d1=t2, d2=t4, d3=t3, d4=t1
#       ...
# 2) when generating the scale, the system must: 
#    2.1) consider the absences of each team and  
#       that there is one team 4 employees/ day
#    2.2) consider hours of workload adjustments 
#
# 3) add up the hours of employees in the month 
#    include in the column "total hours" in the 
#    schedule_table
# 4) use the genetic algorithm to find the best 
#    scale, with setTime to measure the execution 
#    time

def get_employee_absences(absences, team_employee, day):

    for ab in range(len(absences)):
        # employee, type of absence, days of absence
        (emp, toa, doa, hrs) = absences[ab]
        emp = emp['employee']
        toa = toa['type']
        doa = doa['days']
        hrs = hrs['hours']
        
        if emp == team_employee:
            if day in doa:
                return (toa, hrs)
        
    return (0, 0)
        

# generate schedule_table scale with heuristic algorithm
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

    schedule_table['total_Horas'] = schedule_table.sum(axis = 1)

    schedule_table['ideal'] = 168

    return schedule_table



def create_scheduling(schedule_table, days, employees, team_employee, scale_days, absences):
    for day in range(len(days)):
        for employee in range(len(employees)):
                   
            if (employees[employee] == team_employee and day in scale_days):
                
                # employee absences
                (toa, hrs) = get_employee_absences(absences, team_employee, day)
                
                if (toa != 0):
                    schedule_table.iloc[employee, day] = hrs
                else:
                    schedule_table.iloc[employee, day] = 24


if __name__ == '__main__':

    try:
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
    except:
        print('There was an error reading the settings file')

    schedule_tables = []
    df = pandas.DataFrame()

    try:

        for i in range(len(possibilities)):
            
            #print(i)
            #print("------- Possibility -------")
            
            poss = possibilities[i]

            #print(pos)
            #print("---------------------------")

            (first, _, _, _) = possibilities[i]
            (last_team) = last_schedule[0]


            # the last team can't be the first on current month
            if last_team != first:
                schedule_tables = get_schedule_tables(data, poss, days, employees, schedule, absences)
                print(schedule_tables)

                df = pandas.DataFrame([schedule_tables['total_Horas'], schedule_tables['ideal']])

                hours_sum = 0
                for hours in schedule_tables['total_Horas']:
                    hours_sum = hours_sum + hours

                average_hours = hours_sum / len(schedule_tables['total_Horas'])
                print('Média de horas: ', average_hours)
                
    except:
        print("There was an error generating the scale")

    print(df)
    # print(df.corr())
            
    print("fim")


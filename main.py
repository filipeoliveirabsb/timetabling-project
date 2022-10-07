from evaluateSchedule import EvaluateSchedule
from solver import Solver
import pandas as pd
import time
from ruamel.yaml import YAML

# *------------------ RULES ---------------------*
# the intervals between schedules are 3 days long
# optimal number of hours in month / employee=160h
# max hours in month / employee = 40h / week
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
# 4) use a heuristic algorithm to find the best
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

    schedule_table = pd.DataFrame(
        index=data["employees"], columns=days)

    (first, second, third, fourth) = poss

    for k in range(len(schedule)):

        (team, team_employee, _) = schedule[k]

        if team == first:

            (scale_days) = data["scale_days"][0]

            create_scheduling(schedule_table, days, employees,
                              team_employee, scale_days, absences)

        if team == second:

            (scale_days) = data["scale_days"][1]

            create_scheduling(schedule_table, days, employees,
                              team_employee, scale_days, absences)

        if team == third:

            (scale_days) = data["scale_days"][2]

            create_scheduling(schedule_table, days, employees,
                              team_employee, scale_days, absences)

        if team == fourth:

            (scale_days) = data["scale_days"][3]

            create_scheduling(schedule_table, days, employees,
                              team_employee, scale_days, absences)

    schedule_table['total'] = schedule_table.sum(axis=1)

    return schedule_table


def create_scheduling(schedule_table, days, employees, team_employee, scale_days, absences):
    for day in range(len(days)):
        for employee in range(len(employees)):

            if (employees[employee] == team_employee and day in scale_days):

                # employee absences
                (toa, hrs) = get_employee_absences(
                    absences, team_employee, day)

                # at this point we consider legal days off as hours worked
                if (toa == 'AJ'):
                    schedule_table.iloc[employee, day] = hrs
                else:
                    schedule_table.iloc[employee, day] = 24


def final_scheduling(schedule_print, days, employees, absences):
    for day in range(len(days)):
        for employee in range(len(employees)):

            if schedule_print.iloc[employee, day] >= 0:
                for ab in range(len(absences)):
                    # employee, type of absence, days of absence
                    (emp, toa, doa, hrs) = absences[ab]
                    emp = emp['employee']
                    toa = toa['type']
                    doa = doa['days']
                    hrs = hrs['hours']

                    if employees[employee] == emp:

                        if day in doa:
                            # at this point we consider all abesences
                            schedule_print.iloc[employee, day] = toa

    return schedule_print


if __name__ == '__main__':
    start_time = time.time()
    try:
        data_file = "./raw_data.yaml"
        raw_data_file = open(data_file)
        data = YAML().load(raw_data_file.read())
        raw_data_file.close()

        # copy the data
        possibilities = data["order_possibilities"]
        last_schedule = data["last_schedule"]
        months = data["months"]
        employees = data["employees"]
        schedule = data["team_schedule"]

        absences = data["month"]["jun"]["absences"]
    except:
        print('There was an error reading the settings file')

    schedule_table = []
    schedules_generated = []
    data_days = []
    # e.g: jan = 0, feb = 1, ...
    (_, days_t) = months[5]

    for d in range(1, days_t + 1):
        data_days.append(d)

    try:

        for i in range(len(possibilities)):

            #print("------- Possibility -------")

            poss = possibilities[i]

            # print(pos)
            # print("---------------------------")

            (first, second, third, _) = possibilities[i]
            (last_team) = last_schedule[0]

            # the last team selected must rest 72 hours
            if last_team not in (first, second, third):
                schedule_table = get_schedule_tables(
                    data, poss, data_days, employees, schedule, absences)
                # print(schedule_table)

                # call evaluateSchedule to calculate the weekly average
                schedule_evaluated = EvaluateSchedule.calculateWeeklyAverage(
                    schedule_table, data_days)

                # call calculateAdjusts to calculate missing or extra hours
                schedule_adjusts = EvaluateSchedule.calculateAdjusts(
                    schedule_evaluated, data_days)

                # call compensatoryTime to calculate the bank of hours
                schedule_final = EvaluateSchedule.compensatoryTime(
                    schedule_adjusts, employees, data)

                schedules_generated.append(schedule_final)

        # optional
        for s in schedules_generated:
            print(s)

        # instantiate and call the solver to find the best scale(s)
        schedules_final = Solver.get_best_schedule(schedules_generated)

        # print the best schedule(s) with absences:
        print("--------------------------------------------------------------------------------- Best Schedules --------------------------------------------------------------------------------------")
        for s in schedules_final:
            print(final_scheduling(s, data_days, employees, absences))

        # calculate the runtime of the program
        print("---------------------------------------------------------------------------------   Statistics   --------------------------------------------------------------------------------------")
        print('foram geradas', len(schedules_generated),
              'possibilidades de ordem de escala')
        print('foram selecionadas', len(schedules_final),
              'escalas ideais')
        print('Runtime:', round((time.time() - start_time), 5), ' seconds')

    except:
        print("There was an error generating the scale")

    # print("end")

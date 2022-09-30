class EvaluateSchedule:

    def calculateWeeklyAverage(schedule, days):
        #print("calculating weekly average")
        # go through the schedule and calculate the weekly average of each employee
        # calculate the weekly average
        # calculate how many weeks per month. E.g: 30/7 = 4,3 weeks
        try:
            listAverage = []
            total_weeks = round((len(days) / 7), 2)
            
            for i in range(len(schedule['total'])):
                total = schedule['total'][i]
                weekly_average = int(total / total_weeks)
                listAverage.append(weekly_average)

            schedule['wa'] = listAverage

            return schedule

        except:
            print('There was an error on alculating Weekly Average')

    def calculateAdjusts(schedule, days):
        #print("calculating Adjusts")
        # go through the schedule and calculate the missing or extra hours
        
        try:
            listAdjusts = []
            total_weeks = round((len(days) / 7), 2)
            for i in range(len(schedule['wa'])):
                hours_to_adjust = 0
                employee_average = schedule['wa'][i]
                
                hours_to_adjust = int(employee_average - 40) * total_weeks
                listAdjusts.append(hours_to_adjust)

            # inclui a coluna ajustes na schedule
            schedule['adj'] = listAdjusts

            return schedule

        except:
            print('There was an error on calculating Adjusts')

    def compensatoryTime(schedule, employees, data):
        #print("compensatory time adjust")
        # go through the schedule and calculate the compensatory time bank
        
        try:
            over_list = []
            comp_time = data["comp_time"]
            
            for employee in range(len(employees)):
                over = 0
                adjust = schedule['adj'][employee]

                for i in range(len(comp_time)):
                    (emp, hrs) = comp_time[i]
                    emp = emp['employee']
                    hrs = hrs['hours']
                    """ print('-------------- comp_time e employees ---------------')
                    print(emp, hrs)
                    print(employees[employee])
                    print(employees[employee] == emp)
                    print(adjust) """
                    if employees[employee] == emp and adjust != 0:
                        over = hrs + adjust
                        
                over_list.append(over)

            schedule['over'] = over_list

            return schedule

        except:
            print('There was an error on compensatory time adjust')

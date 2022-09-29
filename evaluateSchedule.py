class EvaluateSchedule:

    def calculateWeeklyAverage(schedule, days):
        print("calculating weekly average")
        # percorrer a schedule e calcular a media semanal
        # de cada agente
        # calcular total horas / total semanas
        # calcular quantas semanas / mês. Ex 30/7 = 4,3 semanas
        try: 
            listAverage = []
            total_weeks = round((len(days) / 7), 2)
            # print(total_weeks)

            # quantas horas ele trabalhou a cada 7 dias?
            for i in range(len(schedule['total'])):
                # print(schedule['total'][i])
                total = schedule['total'][i]
                weekly_average = int(total / total_weeks)
                listAverage.append(weekly_average)

            # inclui a coluna media semanal na schedule
            schedule['wa'] = listAverage

            return schedule
        
        except:
            print('There was an error on alculating Weekly Average')

    def calculateAdjusts(schedule, days):
        print("calculating Adjusts")
        # percorrer a schedule e calcular as horas
        # faltantes ou a mais baseado na media semanal
        # a media ideal (40h) vezes o numero de semanas

        try: 
            listAdjusts = []
            total_weeks = round((len(days) / 7), 2)
            for i in range(len(schedule['wa'])):
                hours_to_adjust = 0
                employee_average = schedule['wa'][i]
                # print(employee_average)
                # print(total_weeks)

                hours_to_adjust = int(employee_average - 40) * total_weeks
                listAdjusts.append(hours_to_adjust)

            # inclui a coluna ajustes na schedule
            schedule['adj'] = listAdjusts

            return schedule
        
        except:
            print('There was an error on calculating Adjusts')

    """ def adjustSchedule(schedule, days, employees):
        print("Adjusting schedule")
        listAdjusts = []
        # percorrer a schedule e ajustar cada agente
        # distribuindo as horas sobrantes pelos dias
        # respeitando as regras 24 no max e min 2 de
        # agentes com 24 no dia
        available_days = days
        for day in range(len(days)):
            for employee in range(len(employees)):
                adjusts = schedule.iloc[employee, day]['adjusts']
                hours_in_day = schedule.iloc[employee, day]
                if adjusts > 0:
                    # distribuir as horas considerando dias de folga e alguma regra de utilização de horas (ex. de 8 em 8)
                    # while adjusts > 0:
                    if day in available_days and hours_in_day > 0:
                        schedule.iloc[employee, day] = 8
                        adjusts -= 8

        return schedule """

    def compensatoryTime(schedule, employees, data):
        print("compensatory time adjust")
        # percorrer a schedule e para cada agente alimentar o banco de horas
        # adicionando ou discontando horas

        try:
            over_list = []
            comp_time = data["comp_time"]
            #print(comp_time)
            #print(adjust_list)
            
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
                        #print(over)
                
                over_list.append(over)
                    
            schedule['over'] = over_list

            return schedule

        except:
            print('There was an error on compensatory time adjust')
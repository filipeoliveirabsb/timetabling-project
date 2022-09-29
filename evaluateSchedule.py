class EvaluateSchedule:

    def calculateWeeklyAverage(schedule, days):
        print("Calculating Weekly Average")
        listAverage = []
        # percorrer a schedule e calcular a media semanal
        # de cada agente
        # calcular total horas / total semanas
        # calcular quantas semanas / mês. Ex 30/7 = 4,3 semanas

        total_weeks = round((len(days) / 7), 2)
        # print(total_weeks)

        # quantas horas ele trabalhou a cada 7 dias?
        for i in range(len(schedule['total_hours'])):
            # print(schedule['total_hours'][i])
            total = schedule['total_hours'][i]
            weekly_average = int(total / total_weeks)
            listAverage.append(weekly_average)

        # inclui a coluna media semanal na schedule
        schedule['weekly_average'] = listAverage

        return schedule

    def calculateAdjusts(schedule, days):
        print("Calculating Adjusts")
        listAdjusts = []
        # percorrer a schedule e calcular as horas
        # faltantes ou a mais baseado na media semanal
        # a media ideal (40h) vezes o numero de semanas

        total_weeks = round((len(days) / 7), 2)
        for i in range(len(schedule['weekly_average'])):
            hours_to_adjust = 0
            employee_average = schedule['weekly_average'][i]
            # print(employee_average)
            # print(total_weeks)

            hours_to_adjust = int(employee_average - 40) * total_weeks
            listAdjusts.append(hours_to_adjust)

        # inclui a coluna ajustes na schedule
        schedule['adjusts'] = listAdjusts

        return schedule

    def adjustSchedule(schedule, days, employees):
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

        return schedule

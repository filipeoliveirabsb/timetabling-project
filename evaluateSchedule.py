class EvaluateSchedule:

    def calculateWeeklyAverage(schedule):
        print("Calculating Weekly Average")
        listAverage = []
        # percorrer a schedule e calcular a media semanal
        # de cada agente
        # calcular total horas / total semanas
        # calcular quantas semanas / mês. Ex 30/7 = 4,3 semanas

        # quantas horas ele trabalhou a cada 7 dias?
        for i in range(len(schedule['total_Horas'])):
            total = schedule['total_Horas'][i]
            weekly_average = int(total / 4)
            listAverage.append(weekly_average)

        # inclui a coluna media semanal na schedule
        schedule['weekly_average'] = listAverage

    def calculateAdjusts(schedule):
        print("Calculating Adjusts")
        listAdjusts = []
        # percorrer a schedule e calcular as horas
        # faltantes ou a mais baseado na media semanal
        # a media ideal (40h) vezes o numero de semanas
        for i in range(len(schedule['weekly_average'])):
            hours_to_adjust = 0
            employee_average = schedule['weekly_average'][i]

            hours_to_adjust = int(employee_average - 40) * 4
            listAdjusts.append(hours_to_adjust)

        # inclui a coluna ajustes na schedule
        schedule['adjusts'] = listAdjusts

    def adjustSchedule(schedule, days, employees):
        print("Adjusting schedule")
        listAdjusts = []
        # percorrer a schedule e ajustar cada agente
        # distribuindo as horas sobrantes pelos dias 
        # respeitando as regras 24 no max e min 2 de
        # agentes com 24 no dia
        for day in range(len(days)):
            for employee in range(len(employees)):
                adjusts = schedule.iloc[employee, day]['adjusts']

                # distribuir as horas considerando dias de folga e alguma regra de utilização de horas (ex. de 8 em 8)
                # while adjusts > 0:
                schedule.iloc[employee, day] = 8
                adjusts -= 8

        
        
def __init__(self, schedule, days, employees):
    self.schedule = schedule
    self.days = days
    self.employees = employees
    self.calculateWeeklyAverage(schedule)
    self.calculateAdjusts(schedule)
    self.adjustSchedule(schedule, days, employees)

    return schedule

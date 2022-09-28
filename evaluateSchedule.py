class EvaluateSchedule:

    def calculateWeeklyAverage(schedule):
        print("Calculating Weekly Average")
        listAverage = []
        # percorrer a schedule e calcular a media semanal
        # de cada agente
        # calcular total horas / total semanas
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


def __init__(self, schedule):
    self.schedule = schedule
    self.calculateWeeklyAverage(schedule)
    self.calculateAdjusts(schedule)

    return schedule

class evaluateSchedule:

    def calculateIdeal(schedule):
        print("Calculating Ideal Schedule")
        listIdeal = []
        # percorrer a schedule e calcular quantas semanas o 
        # time trabalhou, o ideal será esse numero * 40
        # para respeitar a regra do ideal de 40h semanais

        # incluir a coluna ideal na lista
        schedule['ideal'] = listIdeal               

    def calculateAdjusts(schedule):
        print("Calculating Adjusts")
        listAdjusts = []
        # percorrer a schedule e calcular as horas
        # faltantes ou a mais baseado no total de horas
        # e a coluca ideal
        schedule['adjusts'] = listAdjusts

    def calculateWeekHours(schedule):
        print("Calculating Week Hours")
        listWeekHours = []
        # percorrer a schedule e calcular a media semanal
        # de cada empregado
        schedule['week_hours'] = listWeekHours

def __init__(self, schedule):
    self.schedule = schedule
    self.calculateIdeal(schedule)
    self.calculateAdjusts(schedule)
    self.calculateWeekHours(schedule)

    return schedule





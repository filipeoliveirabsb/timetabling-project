class Solver:

    def get_best_schedule(schedules, bestSchedule):
        print("Calculating best schedule")

        # percorrer as schedules geradas e compara-las considerando
        # o min de ajustes para o mes seguinte e a média semanal de 
        # cada empregado (se ~= 40)

        # qual das escalas tem média semanal >= 40h por agente com a menor qtd de horas de ajuste? media semanal (melhor para o empregado)

        # qual das escalas possui o maior numero de horas após o ajuste? (melhor para instituição)
        # considerar agora as folgas como não trabalhadas
        # recalcular a coluna total de horas
        # considerar o banco de horas com utilização de 24h, quando houver
        for i in range(len(schedules)):

            total_adjusts = schedules[i].sum(collumn='adj')
            weekly_general_average = schedules[i].sum(collumn='wa')

            # quem tiver a menor qtd de horas de adjusts em módulo e a média semanal mais prox de 40h é melhor escala.
            # o desempate deve considerar:
            # 1) maior número de total_hours
            # 2) menor saldo de banco de horas

            bestSchedule = schedules[i]

    
    def generateWithCompTime(schedules, bestSchedule):
        print("Calculating best schedule")

        # percorrer as schedules geradas e compara-las considerando
        # o min de ajustes para o mes seguinte e a média semanal de 
        # cada empregado (se ~= 40)

        # qual das escalas tem média semanal >= 40h por agente com a menor qtd de horas de ajuste? media semanal (melhor para o empregado)

        # qual das escalas possui o maior numero de horas após o ajuste? (melhor para instituição)
        # considerar agora as folgas como não trabalhadas
        # recalcular a coluna total de horas
        # considerar o banco de horas com utilização de 24h, quando houver
        for i in range(len(schedules)):

            total_adjusts = schedules[i].sum(collumn='adj')
            weekly_general_average = schedules[i].sum(collumn='wa')

            # quem tiver a menor qtd de horas de adjusts em módulo e a média semanal mais prox de 40h é melhor escala.
            # o desempate deve considerar:
            # 1) maior número de total_hours
            # 2) menor saldo de banco de horas

            bestSchedule = schedules[i]


def __init__(self, schedules, bestSchedule):
    self.schedules = schedules
    self.bestSchedule = bestSchedule
    self.get_best_schedule(schedules, bestSchedule)

    return bestSchedule

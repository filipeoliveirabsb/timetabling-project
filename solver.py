class Solver:

    def get_best_schedule(schedules, bestSchedule):
        print("Calculating best schedule")

        # percorrer as schedules geradas e compara-las considerando
        # os ajustes para o mes seguinte e a média semanal de cada
        # empregado (se >= 40)

        # qual das escalas tem média semanal >= 40h por agente com a menor qtd de horas de ajuste?
        for i in range(len(schedules)):

            total_adjusts = schedules[i].sum(collumn='adjusts')
            weekly_general_average = schedules[i].sum(collumn='weekly_average')

            # if weekly_general_average ... and total_adjusts ...
            # ...save i

            bestSchedule = schedules[i]


def __init__(self, schedules, bestSchedule):
    self.schedules = schedules
    self.bestSchedule = bestSchedule
    self.get_best_schedule(schedules, bestSchedule)

    return bestSchedule

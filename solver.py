class Solver:

    def get_best_schedule(schedules):
        #print("calculating best schedule")

        # percorrer as schedules geradas e compara-las considerando nessa ordem:
        try:
            # 1) média geral mais proxima de 40h/semana
            save_best_wa = 0
            best_list = []

            for i in range(len(schedules)):

                schedule_table = schedules[i]

                weekly_general_average = (schedule_table['wa'].sum()) / 16

                # valor absoluto - distancia para o ideal 40
                mod = abs(weekly_general_average - 40)

                """ print('------ procurando melhor media semanal ------')
                print(i)
                print(weekly_general_average)
                print(save_best_wa)
                print(mod)
                print('---------------------------------------------') """

                if save_best_wa == 0:
                    best_list.append(i)
                    save_best_wa = mod
                else:
                    if mod < save_best_wa:

                        for j in range(len(best_list)):
                            best_list.remove(j)

                        best_list.append(i)
                        save_best_wa = mod
                    elif mod == save_best_wa:
                        best_list.append(i)
                        save_best_wa = mod

            # print(best_list)

            # 2) se empate, qual tem menor numero absoluto (módulo) de ajustes em hrs
            save_best_adj = 0
            list_best_adj = []
            if len(best_list) > 1:
                for i in range(len(best_list)):
                    bs = best_list[i]
                    schedule_table = schedules[bs]

                    total_adjusts = schedule_table['adj'].abs().sum()
                    """ print('------ procurando menor ajuste ------')
                    print(i)
                    print(total_adjusts)
                    print(save_best_adj)
                    print('-------------------------------------') """

                    if save_best_adj == 0:
                        list_best_adj.append(bs)
                        save_best_adj = total_adjusts
                    else:
                        if total_adjusts < save_best_adj:

                            for j in range(len(list_best_adj)):
                                list_best_adj.remove(j)

                            list_best_adj.append(bs)
                            save_best_adj = total_adjusts
                        elif total_adjusts == save_best_adj:
                            list_best_adj.append(bs)
                            save_best_adj = total_adjusts

                best_list = list_best_adj

            # print(best_list)

            # 3) se empate, qual tem maior numero de horas (interesse da instituição)
            save_best_total = 0
            list_best_total = []
            if len(best_list) > 1:
                for i in range(len(best_list)):
                    bs = best_list[i]
                    schedule_table = schedules[bs]

                    total_hours = schedule_table['total'].sum()
                    """ print('------ procurando maior total -------')
                    print(i)
                    print(total_hours)
                    print(save_best_total)
                    print('-------------------------------------') """

                    if save_best_total == 0:
                        list_best_total.append(bs)
                        save_best_total = total_hours
                    else:
                        if total_hours > save_best_total:

                            for j in range(len(list_best_total)):
                                list_best_total.remove(j)

                            list_best_total.append(bs)
                            save_best_total = total_hours
                        elif total_hours == save_best_total:
                            list_best_total.append(bs)
                            save_best_total = total_hours

                best_list = list_best_total

            # print(best_list)

            # 4) se empate, qual gera o menor saldo de banco de horas
            save_best_over = 0
            list_best_over = []
            if len(best_list) > 1:
                for i in range(len(best_list)):
                    bs = best_list[i]
                    schedule_table = schedules[bs]

                    total_over = schedule_table['over'].sum()
                    """ print('------ procurando menor banco horas -------')
                    print(i)
                    print(total_over)
                    print(save_best_over)
                    print('-------------------------------------------') """

                    if save_best_over == 0:
                        list_best_over.append(bs)
                        save_best_over = total_over
                    else:
                        if total_over < save_best_over:

                            for j in range(len(list_best_total)):
                                list_best_over.remove(j)

                            list_best_over.append(bs)
                            save_best_over = total_over
                        elif total_over == save_best_over:
                            list_best_over.append(bs)
                            save_best_over = total_over

                best_list = list_best_over

            print(best_list)

            # permanecendo o empate, todas as listas remanecentes devem ser retornadas
            # return the best shcedule(s)
            print('final')
            schedules_final = []
            for i in range(len(schedules)):
                # print(i)
                for j in range(len(best_list)):
                    if i == best_list[j]:
                        schedules_final.append(schedules[i])

            for i in range(len(schedules_final)):
                print(schedules_final[i])

            # return schedules

        except:
            print('There was an error on get best schedule')

    # implementar utilização do banco de horas na v2.
    def generateWithCompTime(schedules, bestSchedule):
        #print("Calculating best schedule")

        # percorrer a(s) melhore(s) schedule(s) geradas e preencher
        # com as ausências em formato mais legível
        # considerar o banco de horas com utilização de 24h, quando houver
        # e o mínimo de 2 agentes por turno
        # recalcular o "over"
        for i in range(len(bestSchedule)):
            print('em desenvolvimento')

class Solver:

    def get_best_schedule(schedules):
        #print("calculating best schedule")

        # go through the scales and compare them, considering:
        try:
            # 1) general average closer to 40h/week
            save_best_wa = 0
            best_list = []

            for i in range(len(schedules)):

                schedule_table = schedules[i]

                weekly_general_average = (schedule_table['wa'].sum()) / 16

                # absolute value - distance to ideal value (40)
                mod = abs(weekly_general_average - 40)
                """ print('------ looking for best weekly average ------')
                print(i)
                print(weekly_general_average)
                print(save_best_wa)
                print(mod)
                print('---------------------------------------------') """

                if save_best_wa == 0:
                    best_list.append(i)
                    save_best_wa = mod
                else:
                    if mod < save_best_wa and len(best_list) > 0:
                        for j in range(len(best_list)):
                            if j in best_list:
                                best_list.remove(j)

                        best_list.append(i)
                        save_best_wa = mod
                    elif mod == save_best_wa:
                        best_list.append(i)
                        save_best_wa = mod

            # print(best_list)

            # 2) if a tie, which one has the lowest absolute number (module) of adjustments in hrs
            save_best_adj = 0
            list_best_adj = []
            if len(best_list) > 1:
                for i in range(len(best_list)):
                    bs = best_list[i]
                    schedule_table = schedules[bs]

                    total_adjusts = schedule_table['adj'].abs().sum()
                    """ print('------ looking for lower fit ------')
                    print(i)
                    print(total_adjusts)
                    print(save_best_adj)
                    print('-------------------------------------') """

                    if save_best_adj == 0:
                        list_best_adj.append(bs)
                        save_best_adj = total_adjusts
                    else:
                        if total_adjusts < save_best_adj and len(list_best_adj) > 0:

                            for j in range(len(list_best_adj)):
                                if j in list_best_adj:
                                    list_best_adj.remove(j)

                            list_best_adj.append(bs)
                            save_best_adj = total_adjusts
                        elif total_adjusts == save_best_adj:
                            list_best_adj.append(bs)
                            save_best_adj = total_adjusts

                best_list = list_best_adj

            # print(best_list)

            # 3) if a tie, which one has the highest number of hours (interest of the institution)
            save_best_total = 0
            list_best_total = []
            if len(best_list) > 1:
                for i in range(len(best_list)):
                    bs = best_list[i]
                    schedule_table = schedules[bs]

                    total_hours = schedule_table['total'].sum()
                    """ print('------ looking for highest total -------')
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
                                if j in list_best_total:
                                    list_best_total.remove(j)

                            list_best_total.append(bs)
                            save_best_total = total_hours
                        elif total_hours == save_best_total:
                            list_best_total.append(bs)
                            save_best_total = total_hours

                best_list = list_best_total

            # print(best_list)

            # 4) if a tie, which one generates the smallest bank of hours balance
            save_best_over = 0
            list_best_over = []
            if len(best_list) > 1:
                for i in range(len(best_list)):
                    bs = best_list[i]
                    schedule_table = schedules[bs]

                    total_over = schedule_table['over'].sum()
                    """ print('------ looking for lower balance -------')
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
                                if j in list_best_over:
                                    list_best_over.remove(j)

                            list_best_over.append(bs)
                            save_best_over = total_over
                        elif total_over == save_best_over:
                            list_best_over.append(bs)
                            save_best_over = total_over

                best_list = list_best_over

            print(best_list)

            # if the tie persists, all remaining schedules must be returned
            # return the best shcedule(s)
            schedules_final = []
            for i in range(len(schedules)):
                for j in range(len(best_list)):
                    if i == best_list[j]:
                        schedules_final.append(schedules[i])

            # optional
            """ for i in range(len(schedules_final)):
                print(schedules_final[i]) """

            return schedules_final

        except:
            print('There was an error on get best schedule')

    # implement bank of hours usage in v2.
    def generateWithCompTime(schedules, bestSchedule):
        #print("Calculating best schedule")
        # consider the bank of hours with 24-hour use, when there is,
        # and the minimum of 2 employees per shift
        for i in range(len(bestSchedule)):
            print('em desenvolvimento')

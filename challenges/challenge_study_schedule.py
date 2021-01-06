def study_schedule(start_time, end_time, target_time):
    """ Faça o código aqui. """
    melhor_horario = 0
    if start_time == '' or target_time == '':
        return 0

    for i in range(len(start_time)):
        if start_time[i] and target_time <= end_time[i]:
            melhor_horario += 1

    return melhor_horario

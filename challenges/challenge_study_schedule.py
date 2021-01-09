""" [Retorne, para uma entrada específica, o melhor horário para disponibilizar
 o conteúdo]

[Retorne, quando mais de um target_time empata com a maior saída, o melhor
horário para disponibilizar o conteúdo]

[Retorne 0 se start_time recebe um valor vazio]

[Retorne 0 se target_time recebe um valor vazio]

[Execute a função, somando 10.000 execuções para uma entrada pequena, em menos
que 0.02s (tempo da execução do avaliador no Pull Request)] """

"""   when target_time = 5
        verify if target_time is >= start_time or end_time is <= target_time
        if yes count add + 1

        return count from function """


def study_schedule(start_time, end_time, target_time):
    if len(start_time) < 1 or target_time == 0:
        return 0
    count = 0
    element = 0
    for time in start_time:

        if target_time >= time:
            if target_time <= end_time[element]:
                count = count + 1
        element = element + 1
    return count

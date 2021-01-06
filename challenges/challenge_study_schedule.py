def study_schedule(start_time, end_time, target_time):
    """ Faça o código aqui. """
    count = 0
    for index in range(len(start_time)):
        if start_time[index] <= target_time <= end_time[index]:
            count += 1

    return count

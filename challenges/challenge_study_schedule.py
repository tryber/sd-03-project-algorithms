def study_schedule(start_time, end_time, target_time):
    cont = 0
    if (len(end_time) != len(start_time)):
        return 0
    for i in range(len(start_time)):
        if (start_time[i] <= target_time <= end_time[i]):
            cont += 1
    return cont

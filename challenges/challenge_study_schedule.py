def study_schedule(start_time, end_time, target_time):
    counter = 0
    for x in range(len(start_time)):
        if target_time in range(start_time[x], end_time[x]+1):
            counter += 1
    return counter

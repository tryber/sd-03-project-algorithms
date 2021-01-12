def study_schedule(start_time, end_time, target_time):
    counter = 0
    for index in range(len(start_time)):
        if target_time >= start_time[index] and target_time <= end_time[index]:
            counter += 1

    return counter

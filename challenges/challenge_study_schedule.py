def study_schedule(start_time, end_time, target_time):
    repeat_quantity = 0
    if (len(start_time) == 0 or len(end_time) == 0 or target_time == 0):
        return repeat_quantity
    for i in range(len(start_time)):
        if (end_time[i] >= target_time >= start_time[i]):
            repeat_quantity += 1
    return repeat_quantity

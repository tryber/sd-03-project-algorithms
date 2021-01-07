def study_schedule(start_time, end_time, target_time):
    if not start_time:
        return 0
    if not target_time:
        return 0
    count = 0
    for i in range(len(start_time)):
        if end_time[i] >= target_time >= start_time[i]:
            count += 1
    return count

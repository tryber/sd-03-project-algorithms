def study_schedule(start_time, end_time, target_time):
    if not target_time or target_time > 12:
        return 0
    count = 0
    for index in range(len(start_time)):
        if start_time[index] <= target_time <= end_time[index]:
            count += 1
    return count

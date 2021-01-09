def study_schedule(start_time, end_time, target_time):

    if len(start_time) < 1 or target_time == 0:
        return 0

    count = 0
    for index, hour in start_time:
        if hour <= start_time and start_time <= end_time[index]:
            count += 1

    return count

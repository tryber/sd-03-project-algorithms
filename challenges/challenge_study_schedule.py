def study_schedule(start_time, end_time, target_time):

    if len(start_time) < 1 or target_time == 0:
        return 0

    count = 0
    index = 0
    for hour in start_time:
        if hour <= start_time[index] and hour <= end_time[index]:
            count += 1
        index += 1

    return count

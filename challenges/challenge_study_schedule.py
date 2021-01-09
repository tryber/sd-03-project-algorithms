def study_schedule(start_time, end_time, target_time):

    if len(start_time) < 1 or target_time == 0:
        return 0

    count = 0
    index = 0
    for hour in start_time:
        if hour < target_time or hour == target_time:
            if target_time < end_time[index] or target_time == end_time[index]:
                count += 1
        index += 1

    return count

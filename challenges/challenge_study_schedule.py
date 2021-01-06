def study_schedule(start_time, end_time, target_time):
    if not end_time or not start_time:
        return 0
    count = 1
    for i in range(start_time):
        if start_time <= target_time <= end_time:
            count += 1

    return count

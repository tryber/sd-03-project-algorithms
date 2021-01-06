def study_schedule(start_time, end_time, target_time):
    if not target_time or target_time > 12:
        return 0
    count = 0
    for index in range(len(start_time)):
        if start_time[index] <= target_time <= end_time[index]:
            count += 1
    return count

# start_time = [2, 1, 2, 1, 4, 4]
# end_time   = [2, 2, 3, 5, 5, 5]

# study_schedule(start_time, end_time, 1)
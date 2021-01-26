def study_schedule(start_time, end_time, target_time):
    best_time = 0
    for i in range(len(start_time)):
        if start_time[i] <= target_time <= end_time[i]:
            best_time += 1
    return best_time
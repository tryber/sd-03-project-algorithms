def study_schedule(start_time, end_time, target_time=0):
    perfect_time = 0
    if target_time == 0 or len(start_time) == 0:
        return perfect_time
    for equal in range(len(start_time)):
        if start_time[equal] <= target_time and end_time[equal] >= target_time:
            perfect_time = perfect_time + 1
    return perfect_time

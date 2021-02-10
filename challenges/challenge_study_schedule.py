def study_schedule(start_time, end_time, target_time):
    if not start_time or not end_time or not target_time:
        return 0
    students = 0
    for i in range(len(start_time)):
        if(start_time[i] <= target_time <= end_time[i]):
            students += 1
    return students

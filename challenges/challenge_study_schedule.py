def study_schedule(start_time, end_time, target_time):
    students_studing = 0
    for i in range(len(start_time)):
        if (start_time[i] <= target_time <= end_time[i]):
            students_studing += 1
    return students_studing

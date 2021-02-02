def study_schedule(start_time, end_time, target_time):
    simultaneous_students = 0

    if (len(start_time) == 0 or len(end_time) == 0 or target_time == 0):
        return simultaneous_students

    for i in range(len(start_time)):
        if (end_time[i] >= target_time >= start_time[i]):
            simultaneous_students += 1

    return simultaneous_students

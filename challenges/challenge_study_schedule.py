def study_schedule(start_time, end_time, target_time):
    if (
        not target_time
        or target_time == 0
        or len(start_time) == 0
        or len(end_time) == 0
    ):
        return 0

    students_online = 0

    for i in range(len(start_time)):
        if start_time[i] == target_time or (
            start_time[i] < target_time and end_time[i] >= target_time
        ):
            students_online += 1

    return students_online


if __name__ == "__main__":
    start_time = [2, 1, 2, 1, 4, 4]
    end_time = [2, 2, 3, 5, 5, 5]
    print(study_schedule(start_time, end_time, 5))
    print(study_schedule(start_time, end_time, 4))
    print(study_schedule(start_time, end_time, 3))
    print(study_schedule(start_time, end_time, 2))
    print(study_schedule(start_time, end_time, 1))
    print(study_schedule([], end_time, 1))
    print(study_schedule(start_time, [], 1))
    print(study_schedule(start_time, end_time, 0))

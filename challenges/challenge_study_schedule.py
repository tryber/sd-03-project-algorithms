# Estudante   1  2  3  4  5  6
# starTime = [2, 1, 2, 1, 4, 4]
# endTime = [2, 2, 3, 5, 5, 5]


def study_schedule(start_time, end_time, target_time):
    target_time_counter = 0

    for i in range(len(end_time)):
        if target_time in range(start_time[i], end_time[i] + 1):
            target_time_counter += 1

    return target_time_counter


# horario = input('Digite o target time: ')
# print(study_schedule(starTime, endTime, int(horario)))

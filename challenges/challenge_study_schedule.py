from collections import defaultdict


# estudante   1  2  3  4  5  6
start_time = [2, 1, 2, 1, 4, 4]
end_time = [2, 2, 3, 5, 5, 5]


def study_schedule(start_time, end_time, target_time):
    time_dict = defaultdict(int)

    for index in range(0, len(start_time)):
        for hour in range(start_time[index], end_time[index] + 1):
            time_dict[hour] += 1

    return time_dict[target_time]


print(study_schedule(start_time, end_time, 45))

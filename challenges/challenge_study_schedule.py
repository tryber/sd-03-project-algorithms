def study_schedule(start_time, end_time, target_time):
    """ Faça o código aqui. """
    best_time = 0
    for i in range(len(start_time)):
        if start_time[i] <= target_time <= end_time[i]:
            best_time += 1
    return best_time


if __name__ == '__main__':
    start_time = [2, 1, 2, 1, 4, 4]
    end_time = [2, 2, 3, 5, 5, 5]

    print(study_schedule(start_time, end_time, 5))
    print(study_schedule(start_time, end_time, 4))
    print(study_schedule(start_time, end_time, 3))
    print(study_schedule(start_time, end_time, 2))
    print(study_schedule(start_time, end_time, 1))

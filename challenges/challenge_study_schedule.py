def study_schedule(start_time, end_time, target_time):
    """ Faça o código aqui. """
    counter = 0
    for i in range(len(start_time)):
        if start_time[i] <= target_time and target_time <= end_time[i]:
            counter += 1

    return counter


if __name__ == "__main__":
    start_time = [2, 1, 2, 1, 4, 4]
    end_time = [2, 2, 3, 5, 5, 5]

    print(study_schedule(start_time, end_time, 5))
    print(study_schedule(start_time, end_time, 1))
    print(study_schedule(start_time, end_time, 2))
    print(study_schedule(start_time, end_time, 4))
    print(study_schedule(start_time, end_time, 3))

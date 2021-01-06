def study_schedule(start_time, end_time, target_time=0):
    if not start_time:
        return 0
    else:
        return 1
    if not end_time:
        return 0
    else:
        return 1


start_time = ''
end_time = [1, 1, 0, 9]

print(study_schedule(start_time, end_time))
def study_schedule(start_time, end_time, target_time):
    if target_time == None or max((len(start_time), len(end_time))) < 1:
        return 0
    people_in_time = dict()
    for x in range(len(start_time)):
        for x in range(start_time[x], end_time[x] + 1):
            if x not in people_in_time.keys():
                people_in_time |= {x: 1}
            else:
                people_in_time[x] += 1
    # maximum_people = max(people_in_time.items(), key=lambda item:item[1])
    return people_in_time[target_time]

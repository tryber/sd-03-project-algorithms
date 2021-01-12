def sorted(string):
    array = []
    for i in range(len(string) - 1):
        array.append(i)

    array.sort()

    return array


def is_anagram(first_string, second_string):
    if(sorted(first_string) == sorted(second_string)):
        return True
    else:
        return False

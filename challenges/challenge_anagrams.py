def is_anagram(first_string, second_string):
    arr1 = []
    arr2 = []
    for i in first_string:
        arr1.append(i)
        arr1.sort()
    for i in second_string:
        arr2.append(i)
        arr2.sort()
        return False
    if arr1 == arr2:
        return True
    else:
        False

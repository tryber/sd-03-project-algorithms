def is_anagram(first_string, second_string):
    # arr1 = []
    # arr2 = []
    # for i in first_string:
    #     arr1.append(i)
    #     arr1.sort()
    # for i in second_string:
    #     arr2.append(i)
    #     arr2.sort()
    # i see this code and i think that isn't good.
    #  so i search in google and i discovered a func sorted()
    string_one = sorted(first_string)
    string_two = sorted(second_string)
    # print(string_one, "junto ", string_two)
    if not first_string or not second_string:
        return False
    if string_one == string_two:
        return True
    else:
        return False

def is_anagram(first_string, second_string):
    string_one = sorted(first_string)
    string_two = sorted(second_string)
    if not first_string or not second_string:
        return False
    if string_one == string_two:
        return True
    else:
        return False

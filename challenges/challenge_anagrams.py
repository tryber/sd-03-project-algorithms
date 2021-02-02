def is_anagram(first_string, second_string):
    first_string = list(first_string)
    second_string = list(second_string)

    if (first_string == [] or second_string == []):
        return False

    if (sorted(first_string) == sorted(second_string)):
        return True

    else:
        return False

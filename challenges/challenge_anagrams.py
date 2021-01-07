def is_anagram(first_string, second_string):
    first_sorted = list(first_string)
    second_sorted = list(second_string)
    first_sorted.sort()
    second_sorted.sort()
    if first_sorted == second_sorted:
        return True
    else:
        return False

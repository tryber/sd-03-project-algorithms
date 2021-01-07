from challenges.sorts.merge_sort_string import merge_sort


def is_anagram(first_string, second_string):
    string_one_sorted = merge_sort(first_string)
    string_two_sorted = merge_sort(second_string)

    if string_one_sorted == string_two_sorted:
        return True
    else:
        return False

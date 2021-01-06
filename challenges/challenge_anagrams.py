from challenges.challenge_find_the_duplicate import merge_sort


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    first_ordenated = merge_sort(first_string)
    second_ordenated = merge_sort(second_string)

    for i in range(len(first_string)):
        if first_ordenated[i] != second_ordenated[i]:
            return False

    return True

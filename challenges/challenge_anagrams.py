def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    return merge(left, right, array.copy())


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) == 0 or len(second_string) == 0:
        return False
    elif len(first_string) != len(second_string):
        return False
    else:
        ordered_string_1 = "".join(merge_sort(list(first_string)))
        ordered_string_2 = "".join(merge_sort(list(second_string)))
        for index in range(len(first_string)):
            if ordered_string_1[index] != ordered_string_2[index]:
                return False
            return True


if __name__ == "__main__":
    first_string = ""
    second_string = ""
    print(is_anagram(first_string, second_string))
    first_string = "amor"
    second_string = "roma"
    print(is_anagram(first_string, second_string))
    first_string = "pedra"
    second_string = "perda"
    print(is_anagram(first_string, second_string))
    first_string = "pato"
    second_string = "tapo"
    print(is_anagram(first_string, second_string))
    first_string = "coxinha"
    second_string = "empada"
    print(is_anagram(first_string, second_string))

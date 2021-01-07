def merge(left, right):

    result = []
    left_cursor, right_cursor = 0, 0

    while len(result) < len(left) + len(right):

        if left[left_cursor] <= right[right_cursor]:
            result.append(left[left_cursor])
            left_cursor += 1
        else:
            result.append(right[right_cursor])
            right_cursor += 1

        if right_cursor == len(right):
            result += left[left_cursor:]
            break

        if left_cursor == len(left):
            result += right[right_cursor:]
            break

    return result


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    return merge(left, right)


def is_anagram(first_string, second_string):
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

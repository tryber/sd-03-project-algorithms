def merge(left, right, merged):

    left_piece, right_piece = 0, 0

    while left_piece < len(left) and right_piece < len(right):

        if left[left_piece] <= right[right_piece]:
            merged[left_piece + right_piece] = left[left_piece]
            left_piece += 1
        else:
            merged[left_piece + right_piece] = right[right_piece]
            right_piece += 1

    for left_piece in range(left_piece, len(left)):
        merged[left_piece + right_piece] = left[left_piece]

    for right_piece in range(right_piece, len(right)):
        merged[left_piece + right_piece] = right[right_piece]

    return merged


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

    return merge(left, right, array.copy())


def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False

    first_order_string = ''.join(merge_sort(list(first_string)))
    second_order_string = ''.join(merge_sort(list(second_string)))

    if first_order_string == second_order_string:
        return True
    else:
        return False

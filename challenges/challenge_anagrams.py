def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2

    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

    return merge(left, right, array.copy())


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


def is_anagram(first_string, second_string):
    first = list(first_string)
    second = list(second_string)

    if merge_sort(second) == merge_sort(first):
        return True
    else:
        return False


print('Should be true:', is_anagram("perna", "penra"))
print('Should be true:', is_anagram('pedra', 'perda'))
print('Should be false:', is_anagram('pedra', 'perdaa'))
print('Should be false:', is_anagram('pedra', ''))
print('Should be false:', is_anagram('', 'pedra'))

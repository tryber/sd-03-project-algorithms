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


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right, arr.copy())


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if not first_string or not second_string:
        return False
    a = "".join(merge_sort(list(first_string)))
    b = "".join(merge_sort(list(second_string)))
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


if __name__ == "__main__":
    a = "pedra"
    b = "perda"
    print(is_anagram(a, b))
    a = 'pedra'
    b = 'pedraaa'
    print(is_anagram(a, b))
    a = ''
    b = 'pedraaa'
    print(is_anagram(a, b))
    a = 'pedraaa'
    b = ''
    print(is_anagram(a, b))

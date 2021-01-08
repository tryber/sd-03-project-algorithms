def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

    return merge(left, right, array.copy())


def merge(left, right, arr):
    print(f"{right=}")
    print(f"{left=}")

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            arr[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            arr[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    for left_cursor in range(left_cursor, len(left)):
        arr[left_cursor + right_cursor] = left[left_cursor]
    for right_cursor in range(right_cursor, len(right)):
        arr[left_cursor + right_cursor] = right[right_cursor]
    return arr


def find_duplicate(nums):
    if not isinstance(nums, list) or len(nums) < 2:
        return False
    sorted_nums = merge_sort(nums)
    for i in range(len(sorted_nums) - 1):
        if not isinstance(sorted_nums[i], int) or sorted_nums[i] < 1:
            return False
        if sorted_nums[i] == sorted_nums[i + 1]:
            return sorted_nums[i]

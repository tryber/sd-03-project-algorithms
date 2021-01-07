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


def find_duplicate(nums):
    if not nums or len(nums) < 2:
        return False

    ordered_nums = merge_sort(nums)

    for i in range(len(ordered_nums) - 1):
        if not isinstance(ordered_nums[i], int) or ordered_nums[i] < 1:
            return False
        if ordered_nums[i] == ordered_nums[i + 1]:
            return ordered_nums[i]

    return False

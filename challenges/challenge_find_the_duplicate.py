from challenges.sorts.merge_sort_array import merge_sort


def find_duplicate(nums):
    ordered_array = merge_sort(nums)

    for i in range(len(nums) - 1):
        if ordered_array[i] == ordered_array[i + 1]:
            return ordered_array[i]

    return False


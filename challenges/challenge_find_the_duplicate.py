def merge_sort(arr):
    arr_size = len(arr)
    if arr_size <= 1:
        return arr

    half = arr_size // 2

    list1, list2 = merge_sort(arr[:half]), merge_sort(arr[half:])

    return merge(list1, list2, arr.copy())


def merge(l1, l2, S):
    size1, size2 = len(l1), len(l2)
    i, j, k = 0, 0, 0

    while i < size1 and j < size2:
        if l1[i] < l2[j]:
            S[k] = l1[i]
            i += 1
        else:
            S[k] = l2[j]
            j += 1
        k += 1

    while i < size1:
        S[k] = l1[i]
        i += 1
        k += 1

    while j < size2:
        S[k] = l2[j]
        j += 1
        k += 1

    return S


def find_duplicate(nums):
    if not nums or type(nums) == str:
        return False

    new_nums = merge_sort(nums)

    for i in range(1, len(nums)):
        if new_nums[i] == new_nums[i - 1]:
            return new_nums[i]

    return False

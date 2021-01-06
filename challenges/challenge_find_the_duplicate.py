def find_duplicate(nums):
    if nums:
        nums = merge_sort(nums)
        for x in range(0, len(nums) - 1):
            if nums[x] == nums[x + 1]:
                return nums[x]
    return False


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        half = len(arr) // 2
        return merge(merge_sort(arr[:half]), merge_sort(arr[half:]))


# merges two sorted arrays
def merge(a, b):
    merged = list()
    while len(a) and len(b):
        highest = a
        if b[0] < a[0]:
            highest = b
        merged.append(highest.pop(0))
    last = a or b
    while last:
        merged.append(last.pop(0))
    return merged

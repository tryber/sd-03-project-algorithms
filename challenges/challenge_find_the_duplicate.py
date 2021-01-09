def find_duplicate(nums):
    if len(nums) < 2:
        return False
    nums.sort()
    pos = 0
    for elem in nums:
        if elem == nums[pos + 1] and elem >= 0:
            return elem
        else:
            pos += 1
            if pos == len(nums) - 1:
                return False


print(find_duplicate([3, 2, 9, 2, 4, 0, 7, 8]))

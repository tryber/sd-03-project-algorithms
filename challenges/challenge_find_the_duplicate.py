def find_duplicate(nums):
    duplicate_num = 0
    nums.sort()

    for index in range(len(nums) - 1):
        if nums[index] == nums[index + 1]:
            duplicate_num = nums[index]

    if duplicate_num != 0:
        return duplicate_num

    else:
        return False

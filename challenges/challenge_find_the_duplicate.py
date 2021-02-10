def find_duplicate(nums):
    for i in range(len(nums)):
        num = nums[0]
        nums = nums[1:]
        if(num in nums):
            return num
    return False

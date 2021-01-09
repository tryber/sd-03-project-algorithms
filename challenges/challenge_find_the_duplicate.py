def find_duplicate(nums):
    if len(nums) < 2 or type(nums) != int:
        return False
    nums.sort()
    pos = 0
    for number in nums:
        if number == nums[pos + 1]:
            return number
        else:
            pos += 1
            if pos == len(nums) - 1:
                return False

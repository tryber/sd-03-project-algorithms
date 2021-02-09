def find_duplicate(nums):
    for i in range(len(nums)):
        numero = nums[0]
        nums = nums[1:]
        if(numero in nums):
            return numero
    return False

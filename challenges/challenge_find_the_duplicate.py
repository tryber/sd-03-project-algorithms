def find_duplicate(nums):
    """ Faça o código aqui. """
    if len(nums) > 1:
        nums.sort()
        for i in range(len(nums) - 1):
            if type(nums[i]) == str or nums[i] < 0:
                return False
            if nums[i] == nums[i + 1]:
                return nums[i]
    return False


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    print(find_duplicate(nums) == 2)
    nums = [3, 1, 3, 4, 2]
    print(find_duplicate(nums) == 3)
    nums = [1, 1, 2]
    print(find_duplicate(nums) == 1)
    nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
    print(find_duplicate(nums) == 7)
    nums = [1]
    print(find_duplicate(nums))
    nums = [-1, -1]
    print(find_duplicate(nums))
    nums = ['a', 'b']
    print(find_duplicate(nums))
    nums = [1, 1]
    print(find_duplicate(nums) == 1)
    nums = [1, 2]
    print(find_duplicate(nums) == 1)

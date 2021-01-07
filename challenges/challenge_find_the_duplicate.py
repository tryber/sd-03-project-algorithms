# feito com a ajuda do gustavo

def find_real_duplicate(nums):
    low = 0
    high = len(nums) - 1
    mid = 0
    while low < high:
        mid = (high + low) // 2
        if nums[mid] == nums[mid + 1] or nums[mid] == nums[mid - 1]:
            return nums[mid]
        elif nums[mid] > mid + 1:
            high = mid - 1
        else:
            low = mid + 1
    return False


def find_duplicate(nums):
    """ Faça o código aqui. """
    try:
        if len(nums) > 1 and nums[0] > 0:
            nums.sort()
            return find_real_duplicate(nums)
        return False
    except TypeError:
        return False


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    print(find_duplicate(nums), 2)
    nums = [3, 1, 3, 4, 2]
    print(find_duplicate(nums), 3)
    nums = [1, 1, 2]
    print(find_duplicate(nums), 1)
    nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
    print(find_duplicate(nums), 7)
    nums = [1]
    print(find_duplicate(nums))
    nums = [-1, -1]
    print(find_duplicate(nums))
    nums = ["a", "b"]
    print(find_duplicate(nums))
    nums = [1, 1]
    print(find_duplicate(nums), 1)
    nums = [1, 2]
    print(find_duplicate(nums), 1)

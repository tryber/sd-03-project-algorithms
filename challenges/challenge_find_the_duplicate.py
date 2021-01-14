def find_duplicate(nums):
    if len(nums) == 0 or len(nums) == 1 or type(nums) == str:
        return False

    nums.sort()

    for i in range(len(nums) - 1):
        if type(nums[i]) == str or nums[i] < 0:
            return False
        if nums[i] == nums[i + 1]:
            return nums[i]

    return False


if __name__ == "__main__":
    print(find_duplicate([]))
    print(find_duplicate([1]))
    print(find_duplicate([-1]))
    print(find_duplicate(["a", "b"]))
    print(find_duplicate([1, 3, 4, 2, 2]))
    print(find_duplicate([3, 1, 3, 4, 2]))
    print(find_duplicate([1, 2]))
    print(find_duplicate([1, 1, 2]))
    print(find_duplicate([3, 1, 2, 4, 6, 5, 7, 7, 7, 8]))

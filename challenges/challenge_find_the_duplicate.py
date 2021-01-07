# Outra solução de O(n)

# if type(nums) != list or len(nums) <= 1:
#     return False

# actual = nums[-1]
# if type(actual) != int or actual < 0:
#     return False

# prox = nums[actual - 1]
# while actual != prox:
#     if type(actual) != int or actual < 0:
#         return False
#     prox, nums[actual - 1], actual = (
#         nums[nums[actual - 1] - 1],
#         actual,
#         prox,
#     )

# return actual


def verify_array_to_find_duplicate(nums):
    try:
        if type(nums) != list or len(nums) <= 1:
            return False

        nums.sort()

        if nums[0] < 0 or type(nums[0]) != int:
            return False

        return nums
    except (TypeError, IndexError):
        return False


def find_duplicate(nums):
    new_nums = verify_array_to_find_duplicate(nums)
    if not new_nums:
        return False

    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if nums[mid - 1] == nums[mid] or nums[mid] == nums[mid + 1]:
            return nums[mid]
        elif nums[mid] > mid + 1:
            high = mid - 1
        else:
            low = mid + 1

    return False


if __name__ == "__main__":
    print(find_duplicate([1, 3, 4, 2, 2]), "2")
    print(find_duplicate([3, 1, 3, 4, 2]), "3")
    print(find_duplicate([1, 1]), "1")
    print(find_duplicate([1, 1, 2]), "1")
    print(find_duplicate([3, 1, 2, 4, 6, 5, 7, 7, 7, 8]), "7")

from challenges.sorts.merge_sort_array import merge_sort


def find_duplicate(nums):
    if type(nums) == list and len(nums) > 1 and type(nums[0]) == int:
        high = len(nums)
        ordered_array = merge_sort(nums)
        low = 1

        while low < high - 1:
            if (
                ordered_array[low] == ordered_array[low - 1]
                or ordered_array[low] == ordered_array[low + 1]
            ):
                return ordered_array[low]
            low += 2

        if nums[0] == nums[1]:
            return nums[0]
        else:
            return False

    return False


nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
# # print(type(nums))

print(find_duplicate(nums))

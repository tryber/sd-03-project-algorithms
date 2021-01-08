from challenges.sorts.merge_sort_array import merge_sort


def find_duplicate(nums):
    if type(nums) == list and len(nums) > 0 and type(nums[0]) == int:
        high = len(nums)

        if high == 2:
            if nums[0] == nums[1]:
                return nums[0]
            else:
                return False

        ordered_array = merge_sort(nums)
        low = 1
        while low < high:
            if ordered_array[low] == ordered_array[low - 1] or ordered_array[low] == ordered_array[low + 1]:
                return ordered_array[low]
            low += 2
        return False
    return False
    #     for i in range(len(nums)):
    #         if ordered_array[i + count] == ordered_array[i + count - 1] or ordered_array[i + count] == ordered_array[i + count + 1]:
    #             return ordered_array[i + count]
    #         count += 1

    #     return False
    # else:
    #     return False


nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
# # print(type(nums))

print(find_duplicate(nums))

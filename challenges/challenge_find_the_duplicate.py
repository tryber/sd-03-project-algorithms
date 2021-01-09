from challenges.challenge_anagrams import merge_sort


def find_duplicate(nums):
    order_nums = merge_sort(nums)
    index = 0

    for number in order_nums:
        if index == (len(order_nums) - 1):
            return False

        if number == order_nums[index + 1]:
            return number

        index += 1

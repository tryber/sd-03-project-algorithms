def merge_sort(word):
    word_size = len(word)
    half = word_size // 2
    if word_size == 1:
        return word

    list1, list2 = merge_sort(word[:half]), merge_sort(word[half:])

    return merge(list1, list2)


def merge(l1, l2):
    size1, size2 = len(l1), len(l2)
    i, j = 0, 0
    S = []

    while i < size1 and j < size2:
        if l1[i] < l2[j]:
            S.append(l1[i])
            i += 1
        else:
            S.append(l2[j])
            j += 1

    while i < size1:
        S.append(l1[i])
        i += 1

    while j < size2:
        S.append(l2[j])
        j += 1

    return S


def find_duplicate(nums):
    if not nums or type(nums) == str:
        return False

    new_nums = merge_sort(nums)

    for i in range(1, len(nums)):
        if new_nums[i] == new_nums[i - 1]:
            return new_nums[i]

    return False

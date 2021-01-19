def merge_sort(word):
    word_size = len(word)
    if word_size <= 1:
        return word

    half = word_size // 2

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


def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False

    first_ordenated = merge_sort(first_string)
    second_ordenated = merge_sort(second_string)

    for i in range(len(first_string)):
        if first_ordenated[i] != second_ordenated[i]:
            return False

    return True

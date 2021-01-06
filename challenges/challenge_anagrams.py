def merge_sort(word):
    word_size = len(word)
    half = word_size // 2
    if word_size == 1:
        return word

    list1, list2 = merge_sort(word[:half]), merge_sort(word[half:])

    return merge(list1, list2)

def merge(l1, l2):
    size1 = len(l1)
    size2 = len(l2)
    S = []
    i, j = 0, 0
    while i < size1 and j < size2:
        if l1[i] < l2[j]:
            S.append(l1[i]) 
            i += 1
        else:
            S.append(l2[j])
            j += 1

    if i < size1:
        for k in range(i, size1):
            S.append(l1[k])
    else:
        for k in range(j, size2):
            S.append(l2[k])

    return S

def is_anagram(first_string, second_string):
    first_ordenated, second_ordenated = merge_sort(first_string), merge_sort(second_string)

    for i in range(len(first_string)):
        if first_ordenated[i] != second_ordenated[i]:
            return False
    
    return True

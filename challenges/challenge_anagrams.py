def partition(array, low, high):
    pivot = array[high]
    i = low
    for j in range(low, high):
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[i], array[high] = array[high], array[low]
    return i


def quick_sort(array, low=0, high=None):
    if (high is None):
        high = len(array) - 1
    if (low < high):
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index - 1)
        quick_sort(array, pivot_index + 1, high)
    return array


def is_anagram(first_string, second_string):
    first_string = list(first_string)
    second_string = list(second_string)
    if (first_string == [] or second_string == []):
        return False
    quick_sort(first_string)
    quick_sort(second_string)
    if (first_string == second_string):
        return True
    else:
        return False

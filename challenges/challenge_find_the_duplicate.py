def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def merge_sort(array):

    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    return merge(left, right, array.copy())


# busca binária, retorna o valor se achado na lista, senão retorna None
def search_value(array, value):
    low_index = 0
    high_index = len(array) - 1

    if high_index < low_index:
        return None

    while high_index >= low_index:
        middle_index = (high_index + low_index) // 2
        if array[middle_index] == value:
            return value
        elif array[middle_index] > value:
            high_index = middle_index - 1
        else:
            low_index = middle_index + 1


def find_duplicate(nums):
    """ Faça o código aqui. """
    # cobre se não houver parametros suficientes ou passar um array vazio
    if not nums or len(nums) < 2:
        return False

    ordered_nums = merge_sort(nums)

    for i in range(len(ordered_nums) - 1):
        # caso algum elemento não seja um inteiro positivo
        if not isinstance(ordered_nums[i], int) or ordered_nums[i] < 1:
            return False
        if ordered_nums[i] == ordered_nums[i + 1]:
            return ordered_nums[i]

    return False


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    print(find_duplicate(nums))
    nums = [3, 1, 3, 4, 2]
    print(find_duplicate(nums))
    nums = [1, 1]
    print(find_duplicate(nums))
    nums = [1, 1, 2]
    print(find_duplicate(nums))
    nums = [8]
    print(find_duplicate(nums))
    nums = [-1, 1]
    print(find_duplicate(nums))
    nums = ["a", "b"]
    print(find_duplicate(nums))
    nums = [-1, -1]
    print(find_duplicate(nums))
    nums = [1, 2]
    print(find_duplicate(nums))
    nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
    print(find_duplicate(nums))

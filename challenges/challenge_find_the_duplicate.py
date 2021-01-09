# nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
# Algoritmos obtidos na teoria de algoritmos de ordenação do Bloco 37.
def merge_sort(array):
    # Ordena o array usando o método de dividir // conquistar
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    return merge(left, right, array.copy())


def merge(left, right, merged):
    # Realiza a fusão dos dois arrays após ordenar as metades
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


def binary_search(array, low_index, high_index, value):
    # A cada iteração, esse algoritmo divide a array original ao meio, compara
    # com o valor encontrado e vai repetindo recursivamente até achar o valor.
    # O array precisa estar ordenado, e para isso jogamos na função merge_sort.
    if high_index < low_index:
        return False

    middle_index = (high_index + low_index) // 2

    if array[middle_index] == value:
        return middle_index
    elif array[middle_index] > value:
        return binary_search(array, low_index, middle_index - 1, value)
    else:
        return binary_search(array, middle_index + 1, high_index, value)


def find_duplicate(nums):
    sorted_nums = merge_sort(nums)
    for po in sorted_nums:
        target = sorted_nums[po]
        if binary_search(sorted_nums, po + 1, po + 2, target) == target:
            return target
        else:
            if po == len(nums) - 2:
                return False


# print(find_duplicate(nums))

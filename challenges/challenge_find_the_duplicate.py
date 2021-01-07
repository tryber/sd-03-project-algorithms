# Código da busca se encontra no material de estudos
def binary_search(array, low_index, high_index, value):
    '''
        array - onde estamos procurando o valor
        low_index - índice de onde iniciaremos nossa busca
        high_index - índice de onde finalizaremos nossa busca
        value - valor a ser procurado
    '''
    # caso base: quando os índices se cruzam.
    # Caso onde a busca terminou e o elemento não foi encontrado
    if high_index < low_index:
        # raise ValueError(f"{value} is not in list")
        return False
    # middle_index é o índice que divide o array formado
    # entre o menor índice (low) e o maior (high)
    middle_index = (high_index + low_index) // 2

    # se encontrou o elemento retorne seu índice
    if array[middle_index] == value:
        return middle_index
    # caso o elemento buscado seja menor que o encontrado,
    # procure somente os anteriores a ele.
    # Fazemos isto modificando o índice maior,
    # para o índice anterior ao meio (middle)
    elif array[middle_index] > value:
        return binary_search(array, low_index, middle_index - 1, value)
    # caso o elemento buscado seja maior que o encontrado,
    # procuramos somente os posteriores a ele.
    # Fazemos isto indicando que o índice menor
    # será o índice posterior ao meio (middle)
    else:
        return binary_search(array, middle_index + 1, high_index, value)


def check_early_exit(nums):
    if len(nums) < 2:
        return False
    if isinstance(nums, str):
        return False

    # Ordena o array
    nums.sort()

    if nums[0] < 0:
        return False
    return True


def find_duplicate(nums):
    result = check_early_exit(nums)
    if not result:
        return False

    for i in range(len(nums)):
        result = binary_search(nums, i + 1, len(nums) - 1, nums[i])
        if result:
            return nums[result]
    return False

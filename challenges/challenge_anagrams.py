# Algoritmo obtido na teoria de algoritmos de ordenação do Bloco 37.
def insertion_sort(array):
    # itera sobre cada valor do array
    for i in range(len(array)):
        current_value = array[i]
        current_position = i
        # enquanto o valor da posição for menor que os elementos a sua esquerda
        while (
            current_position > 0
            and array[current_position - 1] > current_value
        ):
            # move as posições para a direita
            array[current_position] = array[current_position - 1]
            current_position = current_position - 1
        # colocamos o elemento em sua nova posição
        array[current_position] = current_value
    print(array)
    return array


def is_anagram(first_string, second_string):
    if len(first_string) == len(second_string):
        firstList = list(first_string)
        secondList = list(second_string)
        if insertion_sort(firstList) == insertion_sort(secondList):
            return True
    return False


# print(is_anagram('lava', 'vala'))
# print(is_anagram('aproximando', 'apropinguando'))
# print(is_anagram('opencart', 'penocrat'))
# print(is_anagram('', 'penocrat'))

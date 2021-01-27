def insertion_sort(unsorted_list):
    sorted_list = unsorted_list
    for i in range(len(sorted_list)):
        current_value = sorted_list[i]
        current_position = i
        # enquanto o valor da posição for menor que os elementos a sua esquerda
        while (
            current_position > 0
            and sorted_list[current_position - 1] > current_value
        ):
            # move as posições para a direita
            sorted_list[current_position] = sorted_list[current_position - 1]
            current_position = current_position - 1
        # colocamos o elemento em sua nova posição
        sorted_list[current_position] = current_value
    return sorted_list


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    sorted_first_string = insertion_sort([*first_string])
    sorted_second_string = insertion_sort([*second_string])

    is_anagram = False

    for index in range(len(sorted_first_string)):
        if sorted_first_string[index] != sorted_second_string[index]:
            is_anagram = False
            break
        else:
            is_anagram = True

    return is_anagram


print(is_anagram('barco', 'ocrab'))

def insertion_sort(string):
    array = list(string)
    for i in range(len(array)):
        current_value = array[i]
        current_position = i
        while (
            current_position > 0
            and array[current_position - 1] > current_value
        ):
            array[current_position] = array[current_position - 1]
            current_position = current_position - 1
        array[current_position] = current_value
    str1 = ""
    return str1.join(array)

def is_anagram(first_string, second_string):
    first_string = insertion_sort(first_string)
    second_string = insertion_sort(second_string)
    return first_string == second_string
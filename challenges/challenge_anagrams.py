def bubble_sort(array):
    has_swapped = True
    num_of_iterations = 0

    while has_swapped:
        has_swapped = False

        for i in range(len(array) - num_of_iterations - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                has_swapped = True
        num_of_iterations += 1

    return "".join(array)


def get_string_array(string):
    array = []
    for i in range(len(string)):
        array.append(string[i])
    return array


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False

    first_string_array = get_string_array(first_string)
    second_string_array = get_string_array(second_string)

    ordened_first_string = bubble_sort(first_string_array)
    ordened_second_string = bubble_sort(second_string_array)

    if ordened_first_string == ordened_second_string:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_anagram("pedra", "perdaaa"))
    print(is_anagram("pedra", "pedro"))
    print(is_anagram("pedra", "perda"))
    print(is_anagram("", "perda"))
    print(is_anagram("pedra", ""))

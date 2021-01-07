def ordenar_anagrama(first_string, second_string):
    lista1 = []
    list2 = []

    for i in range(len(first_string)):
        lista1.append(first_string[i]).sort()
        return lista1

    for j in range(len(second_string)):
        list2.append(second_string[j]).sort()
        return list2
    if lista1 == list2:
        return True
    else:
        return False


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if first_string == "" or second_string == "":
        return False
    elif len(first_string) != len(second_string):
        return False
    if ordenar_anagrama(first_string) == ordenar_anagrama(second_string):
        return True


"""  codigo com bug passando em
todos os casos sem cumprir
todos os requisitos

    while len(first_string) != len(second_string):
        return False
    else:
        return True """

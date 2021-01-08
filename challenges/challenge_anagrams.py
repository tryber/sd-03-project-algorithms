def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if first_string == "" or second_string == "":
        return False
    if first_string != second_string:
        return False


"""  codigo com bug passando em
todos os casos sem cumprir
todos os requisitos

    while len(first_string) != len(second_string):
        return False
    else:
        return True """

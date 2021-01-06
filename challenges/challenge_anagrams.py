def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    nova_primeira_palavra = first_string.sort()
    nova_segunda_palavra = second_string.sort()

    if first_string == '' or second_string == '':
        return False

    if nova_primeira_palavra == nova_segunda_palavra:
        return True
    else:
        False

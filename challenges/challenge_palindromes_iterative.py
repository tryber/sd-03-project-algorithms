def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if word == '':
        return False
    elif word == word[::-1]:
        return True
    else:
        return False

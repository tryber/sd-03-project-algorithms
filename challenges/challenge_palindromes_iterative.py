def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if len(word) == 0:
        return False
    elif word == word[::-1]:
        return True
    else:
        return False

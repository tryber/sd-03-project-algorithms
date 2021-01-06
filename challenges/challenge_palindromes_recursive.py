def is_palindrome_recursive(word, low, high):
    """ Faça o código aqui. """
    if word == '':
        return False
    elif word == is_palindrome_recursive(word[::- 1]):
        return True
    else:
        return False

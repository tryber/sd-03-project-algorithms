def is_palindrome_recursive(word, low, high):
    """ Faça o código aqui. """
    if word == '':
        return False
    elif [word[::-1]] == is_palindrome_recursive(word[:len(word) - 1]):
        return True
    else:
        return False

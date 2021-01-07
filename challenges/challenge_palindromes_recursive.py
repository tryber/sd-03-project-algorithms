def is_palindrome_recursive(word, low, high):
    """ Faça o código aqui. """
    if len(word) == 0:
        return False
    elif word[low] == word[high] - 1:
        return True
    else:
        return is_palindrome_recursive(word, low + 1, high - 1)

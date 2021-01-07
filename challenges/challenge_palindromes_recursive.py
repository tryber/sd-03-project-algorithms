def is_palindrome_recursive(word, low, high):
    """ Faça o código aqui. """
    if len(word) == 0:
        return False
    if word[low] != word[high]:
        return False
    elif len(word) == 1:
        return True
    elif high < len(word) // 2:
        return True
    else:
        return is_palindrome_recursive(word, low + 1, high - 1)

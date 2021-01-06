def is_palindrome_recursive(word, low, high):
    """ Faça o código aqui. """
    for i in range(word):
        if word == word-1:
            return True
        else:
            return False
    if word == 0:
        return False

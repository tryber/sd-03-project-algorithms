def is_palindrome_recursive(word, low = 0):
    """ Faça o código aqui. """
    last = len(word) - 1 
    if word[low] == word[last]:
        return is_palindrome_recursive(word[0:word[:-1]], )
    elif word[low] != word[last]:
        return False
    else:
        return False


word = "SOCOS"
is_palindrome_recursive(word)
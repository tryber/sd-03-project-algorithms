def is_palindrome_recursive(word, low, high):
    """ Faça o código aqui. """
    if not word or high < 1:
        return False
    last = len(word) - 1
    if len(word) == 1:
        return True
    if word[low] == word[last]:
        return is_palindrome_recursive(word[1:len(word )-1], 0, len(word) - 1)
    elif word[low] != word[last]:
        return False
    else:
        return False


# word = "SOCOS"
# is_palindrome_recursive(word)
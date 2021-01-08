def is_palindrome_recursive(word, low, high):
    """ Faça o código aqui. """
    if len(word) == 0:
        return False
    if low == high:
        return True
    if word[low] != word[high]:
        return False
    return is_palindrome_recursive(word, low + 1, high - 1)


""" # para testes locais
word = "socos"
word = "trybe"
print(is_palindrome_recursive(word, 0, len(word) - 1)) """

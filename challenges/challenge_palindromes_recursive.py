def is_palindrome_recursive(word, low, high):
    """ Faça o código aqui. """
    limite = len(word) // 2
    if not word or word[low] != word[high]:
        return False
    elif low > limite:
        return True
    else:
        return is_palindrome_recursive(word, low + 1, high - 1)


if __name__ == '__main__':
    word = ""
    print(is_palindrome_recursive(word, 0, len(word) - 1))
    word = "AGUA"
    print(is_palindrome_recursive(word, 0, len(word) - 1))
    word = "ANA"
    print(is_palindrome_recursive(word, 0, len(word) - 1))
    word = "SOCOS"
    print(is_palindrome_recursive(word, 0, len(word) - 1))
    word = "REVIVER"
    print(is_palindrome_recursive(word, 0, len(word) - 1))

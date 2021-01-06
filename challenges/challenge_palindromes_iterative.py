def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if not word:
        return False
    len_word = len(word)
    for i in range(len_word):
        if word[i] != word[len_word - 1 - i]:
            return False
    return True


if __name__ == "__main__":
    word = ""
    print(is_palindrome_iterative(word))
    word = "AGUA"
    print(is_palindrome_iterative(word))
    word = "ANA"
    print(is_palindrome_iterative(word))
    word = "SOCOS"
    print(is_palindrome_iterative(word))
    word = "REVIVER"
    print(is_palindrome_iterative(word))

def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    search_limit = len(word) // 2

    if len(word) == 0:
        return False
    for i in range(search_limit):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True


if __name__ == "__main__":
    word = ""
    print(is_palindrome_iterative(word))
    word = "ANA"
    print(is_palindrome_iterative(word))
    word = "AGUA"
    print(is_palindrome_iterative(word))
    word = "SOCOS"
    print(is_palindrome_iterative(word))
    word = "REVIVER"
    print(is_palindrome_iterative(word))
    word = "COXINHA"
    print(is_palindrome_iterative(word))

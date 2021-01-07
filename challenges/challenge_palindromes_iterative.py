def is_palindrome_iterative(word):
    if (word == ''):
        return False
    for index in range(0, len(word)):
        if (word[index] != word[len(word) - 1 - index]):
            return False
    return True

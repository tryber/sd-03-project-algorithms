def is_palindrome_iterative(word):
    size = len(word)
    for i in range(size):
        if word[i] != word[size - 1 - i]:
            return False
    return True

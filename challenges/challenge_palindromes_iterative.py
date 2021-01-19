def is_palindrome_iterative(word):
    size = len(word)
    if size == 0:
        return False
    for i in range(size // 2):
        if word[i] != word[size - 1 - i]:
            return False
    return True

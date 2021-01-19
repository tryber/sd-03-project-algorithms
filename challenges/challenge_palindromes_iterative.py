def is_palindrome_iterative(word):
    for i in range(len(word) // 2):
        if (word[i] != word[len(word) - i - 1]):
            return False
    return not(not word)

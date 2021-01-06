def is_palindrome_iterative(word):
    for x in range(len(word) // 2):
        if word[x] != word[-(x + 1)]:
            return False
    return bool(word)

def is_palindrome_iterative(word):

    if (not word):
        return False
    low = 0
    high = len(word)
    for i in range(len(word) // 2):
        if (word[low] != word[high - 1]):
            return False
        low += 1
        high -= 1
    return True

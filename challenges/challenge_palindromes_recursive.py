def is_palindrome_recursive(word, low, high):
    if (not word):
        return False
    if ((high - 1) - (low + 1) >= 0 and word[low] == word[high]):
        return is_palindrome_recursive(word, low + 1, high - 1)
    return word[low] == word[high]

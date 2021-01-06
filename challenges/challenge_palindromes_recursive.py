def is_palindrome_recursive(word, low, high):
    if not word:
        return False
    if low >= high:
        return True
    if high > low:
        if word[low] == word[high]:
            is_palindrome_recursive(word, low + 1, high - 1)
        else:
            return False

def is_palindrome_recursive(word, low, high):
    if not word:
        return False
    if low >= high:
        return True
    if word[high] == word[low]:
        return is_palindrome_recursive(word, low + 1, high - 1)
    return False

def is_palindrome_recursive(word, low, high):
    if not word:
        return False

    if low == high or low == high - 1:
        return word[low] == word[high]

    return (
        word[low] == word[high] and
        is_palindrome_recursive(word, low + 1, high - 1)
    )

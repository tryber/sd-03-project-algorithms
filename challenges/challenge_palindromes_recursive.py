def is_palindrome_recursive(word, low, high):
    if not word:
        return False
    if word[:: -1] != word:
        return False
    else:
        return low == high and is_palindrome_recursive(word, low, high)

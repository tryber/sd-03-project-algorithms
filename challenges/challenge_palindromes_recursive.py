def is_palindrome_recursive(word, low, high):
    if word == '':
        return False
    if low == high:
        return True
    return is_palindrome_recursive(word[::-1], low, high)

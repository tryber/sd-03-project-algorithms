def is_palindrome_recursive(word, low, high):
    if word == '':
        return False
    if low[0] == high[-1]:
        return True
    return is_palindrome_recursive(word[::-1])

def is_palindrome_recursive(word, low, high):
    if word == '':
        return False
    if len(word) <= 1:
        return True
    if word[0] != word[-1] or word[1] != word[-2]:
        return False

    return is_palindrome_recursive(word[1:-1], 0, len(word) - 1)

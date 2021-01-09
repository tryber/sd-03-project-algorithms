def is_palindrome_recursive(word, low, high):
    if word == '':
        return False
    if word[0] != word[-1] or word[1] != word[-2]:
        return False
    if (len(word) - 1) <= 1:
        return True

    return is_palindrome_recursive(
        word[(low + 2):(high - 2)], (low + 2), (high - 2)
    )

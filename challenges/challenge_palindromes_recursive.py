def is_palindrome_recursive(word, low, high):
    if word == '':
        return False
    elif len(word) <= 1:
        return True
    elif word[low] != word[high]:
        return False

    return is_palindrome_recursive(word[1:-1], 0, len(word) - 3)

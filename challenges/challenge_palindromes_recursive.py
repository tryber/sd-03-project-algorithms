def is_palindrome_recursive(word, low, high):
    if word == '':
        return False
    if len(word) <= 1:
        return True
    if word[low] != word[high]:
        return False

    return is_palindrome_recursive(word[(low + 1):(high - 1)])

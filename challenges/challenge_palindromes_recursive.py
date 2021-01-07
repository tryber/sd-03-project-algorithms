def is_palindrome_recursive(word, low, high):
    if word == '':
        return False
    if word != word[:: -1]:
        return False
    if word == word[:: -1]:
        return True
    return is_palindrome_recursive(word, low, high)

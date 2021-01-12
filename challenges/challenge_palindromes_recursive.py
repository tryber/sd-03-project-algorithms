def is_palindrome_recursive(word, low, high):
    if len(word) == 1:
        return True
    elif (word[0] == word[-1]) and is_palindrome_recursive(word[1:-1]):
        return True
    else:
        return False

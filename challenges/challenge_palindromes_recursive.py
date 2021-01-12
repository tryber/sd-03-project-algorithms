def is_palindrome_recursive(word, low, high):
    if word == '':
        return False
    elif len(word) == 1:
        return True
    elif (
        word[0] == word[-1] and is_palindrome_recursive(word[1:-1], low, high)
    ):
        return True
    else:
        return False

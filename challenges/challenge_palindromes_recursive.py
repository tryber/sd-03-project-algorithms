def is_palindrome_recursive(word, low, high):
    if word == "":
        return False
    elif word[0] == word[-1]:
        if len(word) <= 3:
            return True
        return is_palindrome_recursive(word[1:-1], None, None)
    return False

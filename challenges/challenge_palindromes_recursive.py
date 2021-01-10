def is_palindrome_recursive(word, low, high):
    if word == "":
        return False
    else:
        if len(word) < 2:
            return True
    if word[0] != word[-1]:
        return False
    return is_palindrome_recursive(word[1:-1], 0, len("AGUA") - 1)

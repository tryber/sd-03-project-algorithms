def is_palindrome_iterative(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False

    return is_palindrome_iterative(word[1:-1])

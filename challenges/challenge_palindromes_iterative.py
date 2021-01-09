def is_palindrome_iterative(word):
    if word == '':
        return False
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False

    return is_palindrome_iterative(word[1:-1])

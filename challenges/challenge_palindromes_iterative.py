def is_palindrome_iterative(word):
    if word == '':
        return False
    elif word == word[::-1]:
        return True
    else:
        return False

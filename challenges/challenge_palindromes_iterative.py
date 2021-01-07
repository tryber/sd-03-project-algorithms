def is_palindrome_iterative(word):
    if word != word[::-1]:
        return False
    if word == word[::-1]:
        return True

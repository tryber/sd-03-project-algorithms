# referencia: https://www.w3schools.com/python/python_howto_reverse_string.asp
def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    if word == word[::-1]:
        return True
    else:
        return False
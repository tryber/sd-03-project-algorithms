# referencia: https://www.w3schools.com/python/python_howto_reverse_string.asp
def is_palindrome_iterative(word):
    if word == "":
        return False
    return word == word[::-1]
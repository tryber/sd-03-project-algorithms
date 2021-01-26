# referencia: https://www.w3schools.com/python/python_howto_reverse_string.asp
def is_palindrome_iterative(word):
    word_reverse = word[::-1];
    if len(word) > 0 and word == word_reverse:
        return True
    else:
        return False

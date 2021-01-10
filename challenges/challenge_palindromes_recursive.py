def is_palindrome_recursive(word, low, high):
    if word == "":
        return False
    else:
        return word == word[::-1]



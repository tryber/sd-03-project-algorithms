def is_palindrome_recursive(word, low, high):
    # if not word:
    #     return False
    # if word[:: -1] != word:
    #     return False
    # else:
    #     return low == high and is_palindrome_recursive(word, low, high)
    if len(word) < 2:
        return True
    return low == high and is_palindrome_recursive(
        word[1:len(word) - 1], low, high)


# print(is_palindrome_recursive('asdasdasd', 'a', 'a'))

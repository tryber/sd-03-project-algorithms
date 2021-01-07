def is_palindrome_recursive(word, low, high):
    if not word:
        return False
    # if word[:: -1] != word:
    #     return False
    # else:
    #     return low == high and is_palindrome_recursive(word, low, high)
    # if len(word) == 2:  # base case to stop
    #     return False
    if word[low] == word[high]:
        return is_palindrome_recursive(word, low + 1, high - 1)
    return False

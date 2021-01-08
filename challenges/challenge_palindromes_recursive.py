def is_palindrome_recursive(word, low, high):
    last = len(word) - 1
    if not len(word):
        return False
    if len(word) == 1:
        return True
    elif word[low] == word[last]:
        return is_palindrome_recursive(
            word[1: len(word) - 1], 0, len(word) - 1
        )
    elif word[low] != word[last] or not word or high < 1:
        return False
    else:
        return False

def is_palindrome_recursive(word, low, high):
    limit = len(word) // 2
    if not word or word[low] != word[high]:
        return False
    elif low > limit:
        return True
    else:
        return is_palindrome_recursive(word, low + 1, high - 1)

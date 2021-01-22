def is_palindrome_recursive(word, low, high):
    limit = len(word) // 2
    if not word or word[low] != word[high]:
        return False
    elif low > limit:
        return True
    else:
        return is_palindrome_recursive(word, low + 1, high - 1)


print('Should be true:', is_palindrome_recursive('ANA', 0, len('ANA') -1))
print('Should be true:', is_palindrome_recursive('SOCOS', 0, len('SOCOS') -1))
print('Should be false:', is_palindrome_recursive('faa', 0, len('faa') -1))

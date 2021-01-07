def is_palindrome_recursive(word, low, high):
    if low >= high:
        return True
    else:
        if len(word) > 0 and word[low] == word[high]:
            low += 1
            high -= 1
            is_palindrome_recursive(word, low, high)
        else:
            return False


print(is_palindrome_recursive('AABBAA', 0, 5))

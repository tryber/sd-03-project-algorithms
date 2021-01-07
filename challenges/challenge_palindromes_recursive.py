def is_palindrome_recursive(word, low, high):
    if len(word) == 0:
        return False
    if low >= high:
        return True
    if word[low] == word[high]:
        return is_palindrome_recursive(word, low + 1, high - 1)
    return False


# print(is_palindrome_recursive('AABCBAAB', 0, 7))
# print(is_palindrome_recursive('ABACATE', 0, 6))
# print(is_palindrome_recursive('ACAIACA', 0, 6))
# print(is_palindrome_recursive('', 0, -1))

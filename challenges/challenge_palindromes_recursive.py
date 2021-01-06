def is_palindrome_recursive(word, low = 0, high = 0):
    if not word:
        return False
    if low == high or low == high - 1:
        return word[low] == word[high]
    
    return word[low] == word[high] or is_palindrome_recursive(word, low + 1, high - 1)

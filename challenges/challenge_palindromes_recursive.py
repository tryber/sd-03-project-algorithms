def is_palindrome_recursive(word, low, high):
    is_palindrome = False
    if(word == '' or word[low] != word[high]):
        return False
    if(word[low] == word[high]):
        is_palindrome = True
        if(low != high):
            return is_palindrome_recursive(word, low + 1, high - 1)
    return is_palindrome

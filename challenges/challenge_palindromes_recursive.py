def is_palindrome_recursive(word, low, high):
    if len(word) <= 1:
        return True
    else:
        return low == high and is_palindrome_recursive(word[1: -1], low, high)
    

# print(is_palindrome_recursive('natan','n', 'n'));

def is_palindrome_recursive(word, low, high):
    print(high)
    if high == 0:
        print('teste')
        return True
    elif word[low] == word[high]:
        low += 1
        high -= 1
        return is_palindrome_recursive(word, low, high)
    else:
        return False  

print(is_palindrome_recursive('ovjo', 0, 3))

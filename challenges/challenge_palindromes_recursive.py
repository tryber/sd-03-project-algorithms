def is_palindrome_recursive(word, low, high):
    print(high)
    if word == "":
        return False
    if high == 0:
        return True
    elif word[low] == word[high]:
        low += 1
        high -= 1
        return is_palindrome_recursive(word, low, high)
    else:
        return False

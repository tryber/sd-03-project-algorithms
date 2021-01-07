def is_palindrome_iterative(word):
    low = 0
    high = len(word) - 1
    if not word:
        return False
    for i in range(len(word)):
        if low >= high:
            return True
        if word[high] == word[low]:
            low = low + 1
            high = high - 1
    return False


print(is_palindrome_iterative("marcoocram"))

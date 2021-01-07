def is_palindrome_recursive(word, low, high):
    if not word:
        return False
    if len(word) < 2:
        return True
    return (word[0] == word[-1] and is_palindrome_recursive(
        word[1:len(word)-1], low, high))

def is_palindrome_iterative(word):
    if not word:
        return False
    for i in range(len(word)):
        left, right = word[i], word[len(word) - i - 1]
        mid = len(word) // 2
        if i >= mid:
            return True
        if left != right:
            return False

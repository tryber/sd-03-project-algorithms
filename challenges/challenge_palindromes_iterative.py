def is_palindrome_iterative(word):
    if not word:
        return False
    for i in range(len(word)):
        left, right = word[i], word[len(word) - i - 1]
        print(left, right)
        mid = len(word) // 2
        if i >= mid:
            return True
        if left != right:
            return False


is_palindrome_iterative("ABBA")

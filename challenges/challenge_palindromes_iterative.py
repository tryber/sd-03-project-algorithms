def is_palindrome_iterative(word):
    cli = 0  # Current letter index
    lli = len(word) - 1  # Last letter index
    palindrome = True
    if not word:
        return False
    while cli < lli:
        palindrome = palindrome and word[cli] == word[lli]
        cli += 1
        lli -= 1
    return palindrome


print(is_palindrome_iterative('AABCBAAB'))
print(is_palindrome_iterative('ABACATE'))
print(is_palindrome_iterative('ACAIACA'))
print(is_palindrome_iterative('AABBAA'))
print(is_palindrome_iterative(''))

def is_palindrome_iterative(word):
    cur = 0
    last = len(word) - 1
    palindrome = True
    if not word:
        return False
    while cur < last:
        palindrome = palindrome and word[cur] == word[last]
        cur += 1
        last -= 1
    return palindrome

# I had a similar function in javascript about
# palindromes so I've tried to convert it to python.
# also, comment line too long?


print(is_palindrome_iterative('socorrammesubinoonibusemmarrocos'))

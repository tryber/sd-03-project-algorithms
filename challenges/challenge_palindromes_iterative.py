"""
def is_palindrome_iterative(word):
    if word == '':
        return False
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False

    return is_palindrome_iterative(word[1:-1])
"""


def is_palindrome_iterative(word):
    if word == '':
        return False

    cover = len(word) - 1
    index = 0

    while index < cover:
        if word[index] != word[(cover - index)]:
            return False
        if index == (cover // 2):
            return True
        index += 1

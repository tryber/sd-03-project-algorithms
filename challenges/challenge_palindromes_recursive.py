import math


# Me baseei no código em https://github.com/tryber/sd-03-project-algorithms/blob/king-urek-algorithm/challenges/challenge_palindromes_recursive.py e não consegui pensar em uma forma mais elegante de apresentar
def is_palindrome_recursive(word, low, high):
    if not word:
        return False
    equal = word[low] == word[high]

    if len(word) == 1:
        return True

    if low == math.ceil(len(word)/2):
        return equal

    if equal and is_palindrome_recursive(
        word, low + 1, high - 1
    ):
        return True
    else:
        return False

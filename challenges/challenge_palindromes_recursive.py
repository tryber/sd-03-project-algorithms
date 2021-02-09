import math;

def is_palindrome_recursive(word, low, high):
    if not word:
        return False
    letters_is_equal = word[low] == word[high];

    if len(word) == 1:
        return True

    if low == math.ceil(len(word)/2):
        return letters_is_equal

    if letters_is_equal and is_palindrome_recursive(
        word, low + 1, high - 1
    ):
        return True
    else:
        return False



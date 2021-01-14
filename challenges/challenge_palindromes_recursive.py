def is_palindrome_recursive(word, low, high):
    if not word:
        return False
    elif len(word) == 1:
        return True
    elif low == len(word) - 1:
        return word[low] == word[high]
    elif word[low] == word[high] and is_palindrome_recursive(
        word, low + 1, high - 1
    ):
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_palindrome_recursive("", 0, len("") - 1))
    print(is_palindrome_recursive("ANA", 0, len("ANA") - 1))
    print(is_palindrome_recursive("SOCOS", 0, len("SOCOS") - 1))
    print(is_palindrome_recursive("AGUA", 0, len("AGUA") - 1))

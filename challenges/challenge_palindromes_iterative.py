def is_palindrome_iterative(word):
    if not word:
        return False

    reverse_word = ""

    for i in range(len(word) - 1, -1, -1):
        reverse_word += word[i]

    return True if reverse_word == word else False


if __name__ == "__main__":
    print(is_palindrome_iterative(""))
    print(is_palindrome_iterative("ANA"))
    print(is_palindrome_iterative("SOCOS"))
    print(is_palindrome_iterative("AGUA"))

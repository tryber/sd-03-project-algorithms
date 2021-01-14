def is_palindrome_iterative(word):
    if not word:
        return False

    for i in range(len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            return False

    return True


if __name__ == "__main__":
    print(is_palindrome_iterative(""))
    print(is_palindrome_iterative("ANA"))
    print(is_palindrome_iterative("SOCOS"))
    print(is_palindrome_iterative("AGUA"))

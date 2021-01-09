def is_palindrome_iterative(word):
    if word == '':
        return False

    cover = len(word) - 1
    index = 0

    while index < (cover // 2):
        if word[index] != word[(cover - index)]:
            return False

        index += 1

    return True

def is_palindrome_recursive(word, low, high):
    if word == '':
        return False

    cover = high - low
    index = 0

    while index < (cover // 2):
        if word[(low + index)] != word[(high - index)]:
            return False

        index += 1

    return True

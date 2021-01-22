def is_palindrome_iterative(word):
    if not word:
        return False
    word_length = len(word)
    for i in range(word_length // 2):
        if word[i] != word[word_length - 1 - i]:
            return False
    return True

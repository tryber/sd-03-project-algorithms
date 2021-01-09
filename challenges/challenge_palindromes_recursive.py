def is_palindrome_recursive(word, low, high):
    if word == "":
        return False
    else:
        charactere_list = list(word)
        return organize_word(charactere_list)


def organize_word(charactere_list):
    inverted_word = ""
    original_order_word = ""
    for letter in charactere_list:
        original_order_word += letter
    letter_index = len(charactere_list) - 1
    for letter in charactere_list:
        inverted_word += charactere_list[letter_index]
        letter_index = letter_index - 1
    if inverted_word == original_order_word:
        return True
    elif not inverted_word == original_order_word:
        return False


is_palindrome_recursive("", 0, len("") - 1)

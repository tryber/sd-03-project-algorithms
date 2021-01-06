def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if not first_string or not second_string:
        return False
    a = "".join(sorted(first_string))
    b = "".join(sorted(second_string))
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


if __name__ == '__main__':
    a = 'pedra'
    b = 'perda'
    print(is_anagram(a, b))
    a = 'pedra'
    b = 'pedraaa'
    print(is_anagram(a, b))
    a = ''
    b = 'pedraaa'
    print(is_anagram(a, b))
    a = 'pedraaa'
    b = ''
    print(is_anagram(a, b))

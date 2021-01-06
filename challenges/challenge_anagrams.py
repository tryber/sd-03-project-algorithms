def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    anagram = []
    if first_string == '' or second_string == '':
        return False

    for i in range(len(first_string)):
        for j in range(len(first_string)):
            if second_string[j] == first_string[i]:
                anagram[j] = first_string[i]
                return True
            else:
                return False

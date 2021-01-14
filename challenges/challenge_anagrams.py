def is_anagram(first_string, second_string):
    is_anag = False
    if(first_string == '' or second_string == ''):
        return is_anag
    if(sorted(first_string) == sorted(second_string)):
        is_anag = True
        return is_anag
    return is_anag


first_string = "pedra"
second_string = "pedro"
is_anagram(first_string, second_string)

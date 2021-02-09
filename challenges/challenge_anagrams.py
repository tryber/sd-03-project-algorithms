def is_anagram(first_string, second_string):
    if(len(first_string) != len(second_string) or len(first_string) == 0):
        return False
    
    if(len(first_string) == 1 and first_string[0] == second_string[0]):
        return True

    letter = second_string.find(first_string[0])
    if letter == -1:
       return False
    if len(first_string) == 0:
        return True
    else:
       new_first = first_string[1:]
       new_second = second_string[:letter] + second_string[letter+1:]
       return is_anagram(new_first, new_second)

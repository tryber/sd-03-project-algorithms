
def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False
    else:
        first_string_list = list(first_string)
        first_string_list.sort()
        second_string_ist = list(second_string)
        second_string_ist.sort()
        if first_string_list == second_string_ist:
            return True
        else:
            return False

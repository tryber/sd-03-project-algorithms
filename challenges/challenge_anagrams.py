# Ref.: http://bit.ly/39emuam
def check_sum(s1, s2):
    # Criação de dois contadores
    d1 = 0
    d2 = 0
    # roda as strings calculando a soma numérica de cada uma
    for i in range(len(s1)):
        d1 = d1 + ord(s1[i])
        d2 = d2 + ord(s2[i])
    if d1 == d2:
        return True
    return False


def is_anagram(first_string, second_string):
    if len(first_string) == 0 or len(second_string) == 0:
        return False
    if len(first_string) == len(second_string):
        return check_sum(first_string, second_string)
    else:
        return False


print(is_anagram("amor", "roma"))

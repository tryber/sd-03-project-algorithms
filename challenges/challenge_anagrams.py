# O melhor jeito de resolver o problema com anagramas é usando a função
#  checksum
#
# Ref.: http://bit.ly/39emuam
# def check_sum(s1, s2):
#     # Criação de dois contadores
#     d1 = 0
#     d2 = 0
#     # roda as strings calculando a soma numérica de cada uma
#     for i in range(len(s1)):
#         d1 = d1 + ord(s1[i])
#         d2 = d2 + ord(s2[i])
#     if d1 == d2:
#         return True
#     return False
#
#
# def is_anagram(first_string, second_string):
#     if len(first_string) == 0 or len(second_string) == 0:
#         return False
#     if len(first_string) == len(second_string):
#         return check_sum(first_string, second_string)
#     else:
#         return False


# Esta função está no material do curso
def merge_sort(str):
    array = list(str)
    # caso base: se já atingiu a menor porção (1)
    if len(array) <= 1:
        # retorne o array
        return array
    # calculo do pivot: índice que indica onde o array será particionado
    # no caso, metade
    mid = len(array) // 2
    # para cada metade do array
    # chama a função merge_sort de forma recursiva
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    # mistura as partes que foram divididas
    return merge(left, right, array.copy())


# função auxiliar que realiza a mistura dos dois arrays
def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0

    # enquanto nenhumas das partes é percorrida por completo
    while left_cursor < len(left) and right_cursor < len(right):

        # compare os dois itens das partes e insira no array de mistura o menor
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    # a iteração acima irá inserir os elementos de forma ordenada

    # quando uma das partes termina, devemos garantir
    # que a outra sera totalmente inserida no array de mistura

    # itera sobre os elementos restantes na partição "esquerda"
    # inserindo-os no array de mistura
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    # itera sobre os elementos restantes na partição "direita"
    # inserindo-os no array de mistura
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def is_anagram(first_string, second_string):
    if len(first_string) == 0 or len(second_string) == 0:
        return False
    if len(first_string) == len(second_string):
        if merge_sort(first_string) == merge_sort(second_string):
            return True
        else:
            return False
    else:
        return False

def merge_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
   
    left, right = merge_sort(string[:mid]), merge_sort(string[mid:])

    new_string = string[:]
    return merge(left, right, new_string)


# função auxiliar que realiza a mistura dos dois arrays
def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    # enquanto nenhumas das partes é percorrida por completo
    while left_cursor < len(left) and right_cursor < len(right):

        # compare os dois itens das partes e insira no array de mistura o menor
        if left[left_cursor] <= right[right_cursor]:
            merged = merged[:left_cursor + right_cursor] + left[left_cursor] + merged[left_cursor + right_cursor + 1:]
            left_cursor += 1
        else:
            merged = merged[:left_cursor + right_cursor] + right[right_cursor] + merged[left_cursor + right_cursor + 1:] 
            right_cursor += 1
    # a iteração acima irá inserir os elementos de forma ordenada

    # quando uma das partes termina, devemos garantir
    # que a outra sera totalmente inserida no array de mistura

    # itera sobre os elementos restantes na partição "esquerda"
    # inserindo-os no array de mistura
    for left_cursor in range(left_cursor, len(left)):
        merged = merged[:left_cursor + right_cursor] + left[left_cursor] + merged[left_cursor + right_cursor + 1:]

    # itera sobre os elementos restantes na partição "direita"
    # inserindo-os no array de mistura
    for right_cursor in range(right_cursor, len(right)):
        merged = merged[:left_cursor + right_cursor] + right[right_cursor] + merged[left_cursor + right_cursor + 1:]

    return merged

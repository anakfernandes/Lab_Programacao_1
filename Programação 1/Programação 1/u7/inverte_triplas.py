def inverte3a3(s):  # recebe uma string de caracteres como parâmetro
    # separamos em blocos de tres caracteres e colocaremos dentro de uma lista
    lista_blocos = []
    bloco = ''
    for elemento in s:
        if len(bloco) < 3:
            bloco += elemento
            if len(bloco) == 3:
                lista_blocos.append(bloco)
        else:
            bloco = ''
            bloco += elemento
    # invertemos os blocos simetricamente
    for i in range(len(lista_blocos) // 2):
        lista_blocos[i], lista_blocos[len(lista_blocos) - 1 - i] = lista_blocos[len(lista_blocos) - 1 - i], lista_blocos[i]
    # transformamos a lista em string
    str_s_invertido = ''
    for token in lista_blocos:
        str_s_invertido += token

    return str_s_invertido


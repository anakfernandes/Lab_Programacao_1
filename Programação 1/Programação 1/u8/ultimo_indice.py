# Último Índice

#Escreva a função ultimo_indice(num, lista) que recebe um inteiro e uma lista de inteiros
# e que retorna o índice da última ocorrência de num na lista.

# Caso num não esteja na lista, a função deve retornar -1.

def ultimo_indice(num, lista):
    indice = -1
    for i in range(len(lista)):
        if lista[i] == num:
            indice = i

    return indice


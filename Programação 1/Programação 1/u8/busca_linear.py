# Busca Linear

# Escreva a função busca(seq, valor) que implementa o algoritmo de busca linear. Em caso
# de elementos repetidos, deve-se buscar o primeiro da lista. Veja os asserts abaixo, para
# entender a semântica da função.

def busca(seq, valor):

    indice = -1
    for i in range(len(seq) - 1, - 1, - 1):  # caminhando sobre a lista de forma reversa
        if seq[i] == valor:
            indice = i

    return indice

# Rotaciona Array

# Escreva a função rotdir(array) que faz uma rotação circular dos elementos do array
# uma posição à direita. A rotaçao circular consiste em deslocar todos os elementos uma
# posição à direita, exceto o último que deve passar à primeira posição do array.

def rotdir(array):
# troca o elemento que está na última posição pelo elemento que está na primeira posição disponível
    for i in range(len(array) - 1):  # O i assume o índice da primeira posição disponível
        array[i], array[len(array) - 1] = array[len(array) - 1], array[i]

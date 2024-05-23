# Inserção ordenada do primeiro elemento de uma lista

# Implemente a função insere_ordenado_primeiro(lista) que posiciona o primeiro elemento
# da lista recebida como parâmetro de forma a ordená-la. A lista de entrada sempre está
# ordenada de forma crescente (exceto pelo primeiro número).


def insere_ordenado_primeiro(lista):
    j = 0  # índice do elemento, que começa sendo o primeiro da lista
#  Troque o elemento pelo vizinho da direita e repita enquanto o elemento não chegar na
#  última posição da lista e enquanto o seu vizinho da direita for menor que ele
    while j < len(lista) - 1 and lista[j + 1] < lista[j]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
        j += 1



# Merge Invertido

# Escreva a função merge_invertido(l1, l2) que recebe duas listas de inteiros ordenados
# de forma crescente. A função produz e retorna uma nova lista contendo os elementos das
# listas ordenados de forma decrescente

def merge_invertido(l1, l2):  # recebe duas listas de inteiros ordenados de forma crescente
    nova_lista = []  # ordenada de forma decrescente
    i = len(l1) - 1  # caminhar em l1 (começa a partir do último elemento da lista 1)
    j = len(l2) - 1  # caminhar em l2 (começa a partir do último elemento da lista 2)

    while i >= 0 and j >= 0:
        if l1[i] >= l2[j]:
            nova_lista.append(l1[i])
            i -= 1
        else:
            nova_lista.append(l2[j])
            j -= 1
    # descobrindo a lista que chegou no final
    if i < 0:
        for k in range(j, 0 - 1, - 1):
            nova_lista.append(l2[k])
    else:
        for k in range(i, 0 - 1, - 1):
            nova_lista.append(l1[k])

    return nova_lista


l1 = [8, 12, 78, 79, 511]
l2 = [7, 8, 121, 302]
assert merge_invertido(l1, l2) == [511, 302, 121, 79, 78, 12, 8, 8, 7]
print(merge_invertido(l1, l2))
assert l1 == [8, 12, 78, 79, 511]
assert l2 == [7, 8, 121, 302]
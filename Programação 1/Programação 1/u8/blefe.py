# Blefe

# Escreva a função blefe(lista) que recebe uma lista de números inteiros e que altera os
# valores de alguns de seus elementos fazendo com que a lista fique em ordem decrescente.
# Assim, se um elemento não é menor que o anterior, ele deve ser substituído por valor
# igual ao anterior, garantindo a ordem. O processo deve ser repetido até o final da lista.

def blefe(lista):
    nova_lista = []
    if len(lista) > 0:  # Caso a lista não seja vazia
        nova_lista = [0]
        contador = 0
        for i in range(1, len(lista)):
            if lista[i] > lista[i - 1]:
                lista[i] = lista[i - 1]
                contador += 1
                nova_lista.append(contador)
            else:
                nova_lista.append(0)

    return nova_lista


l1 = [9, 4, 5, 3, 1]
assert blefe(l1) == [0, 0, 1, 0, 0]
assert l1 == [9, 4, 4, 3, 1]

l2 = [15, 9, 4, 4, 5, 2, 1, 3, 4]
assert blefe(l2) == [0, 0, 0, 0, 1, 0, 0, 2, 3]
assert l2 == [15, 9, 4, 4, 4, 2, 1, 1, 1]

l3 = [15, 9]
assert blefe(l3) == [0, 0]
assert l3 == [15, 9]

l4 = []
assert blefe(l4) == []
assert l4 == []

l5 = [4]
assert blefe(l5) == [0]
assert l5 == [4]

l6 = [15, 15, 15, 15]
assert blefe(l6) == [0, 0, 0, 0]
assert l6 == [15, 15, 15, 15]

l6 = [1, 2, 3, 4]
assert blefe(l6) == [0, 1, 2, 3]
assert l6 == [1, 1, 1, 1]

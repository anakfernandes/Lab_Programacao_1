def remove_multiplos_do_menor(lista):

    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]


    for i in range(len(lista) - 1, -1, -1):
        if lista[i] % menor == 0:
            lista.pop(i)

l1 = [6, 9, 10, 3, 5]
l2 = [10, 20, 5, 24, 31]
assert remove_multiplos_do_menor(l1) == None
assert remove_multiplos_do_menor(l2) == None
assert l1 == [10, 5]
assert l2 == [24, 31]


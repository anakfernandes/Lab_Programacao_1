# Interseção de Listas

def intersecao_listas(lista1, lista2):

    iguais = []
    for elemento in lista1:

        existencia = False
        for i in range(len(lista2)):
            if elemento == lista2[i]:
                existencia = True

        if existencia:
            iguais.append(elemento)

    lista1 = iguais

    print(lista1)


lista1 = [2, 1, 3, 4]
lista2 = [2]
intersecao_listas(lista1, lista2)


#lista1 = [1, 3, 4]
#lista2 = [4, 3]
#intersecao_listas(lista1, lista2)
#assert lista1 == [3, 4]

#lista1 = [2, 4, 1]
#lista2 = [1, 3, 4]
#intersecao_listas(lista1, lista2)
#assert lista1 == [4, 1]


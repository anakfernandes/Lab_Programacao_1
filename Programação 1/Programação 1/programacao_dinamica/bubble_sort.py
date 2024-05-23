def bubble_sort(lista):
    for j in range(len(lista) - 1):  # Se fizermos o procedimento abaixo len(lista) - 1 com certeza teremos uma lista ordenada no final
        for i in range(len(lista) - 1):  # Pois estamos comparando um número com o seu vizinho da direita
            if lista[i] > lista[i + 1]:  # se o elemento da direita for menor que o elemento da esquerda
                lista[i], lista[i + 1] = lista[i + 1], lista[i]  # troque-os de lugar


lista = [3,5,1,7,8]
bubble_sort(lista)
print(lista)
def insertion_sort(lista):
    for i in range(1, len(lista)):  # começamos a partir do segundo elemento da lista
        chave = lista[i]
        j = i - 1  # representa a parcela da lista que já está ordenada
        while j >= 0 and lista[j] > chave:  # enquanto eu tiver indices à esquerda para olhar e enquanto o lista[j] > chave
            lista[j + 1] = lista[j]  # passando o número que é maior que a chave para trás
            j -= 1  # esse decremento permite comparar a chave com os elementos da lista ordenada
        lista[j + 1] = chave  # posição que podemos inserir a chave. Somamos 1 por causa do decremento da lista acima


lista = [4, 7, 2, 5, 4, 0]
insertion_sort(lista)
print(lista)
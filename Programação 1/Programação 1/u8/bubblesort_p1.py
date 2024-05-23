def bubblesort(dados):
    for j in range(len(dados) - 1):  # Se fizermos o procedimento abaixo len(lista) - 1 com certeza teremos uma lista ordenada no final
        for i in range(len(dados) - 1):  # Pois estamos comparando um número com o seu vizinho da direita
            if dados[i] > dados[i + 1]:  # se o elemento da direita for menor que o elemento da esquerda
                dados[i], dados[i + 1] = dados[i + 1], dados[i]  # troque-os de lugar

# Ordena 3 cores (Vermelho, preto e branco)


def ordena_vpb(lista):  # Inspirado no bubble sort
    for j in range(len(lista) - 1):  # Se fizermos o procedimento abaixo len(lista) - 1 com certeza teremos uma lista ordenada no final
        for i in range(len(lista) - 1):  # Pois estamos comparando um número com o seu vizinho da direita
            if lista[i] == 'p':
                if lista[i + 1] == 'v':
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
            if lista[i] == 'b':
                if lista[i + 1] == 'v':
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                if lista[i + 1] == 'p':
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]

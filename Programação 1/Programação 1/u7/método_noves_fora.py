# Uma Variação do Método Noves Fora

# Tirar os noves é somar os algarismos do número, dois a dois, sempre tirando os noves.
# Uma possível implementação desse método é ordenar de forma decrescente os algarismos
# do número (usar uma lista para manter os algarismos ordenados) e proceder a soma dos
# dois primeiros algarismos que seriam retirados da lista com os algarismos. O valor
# resultante do método noves fora aplicado a esta soma seria inserido na lista, mantendo
# a ordenação.

# Escreva a função noves_fora(lista) que recebe uma lista ordenada de forma decrescente
# com os algarismos de um número e que determina o valor resultante do método noves fora.
# A função além de retornar o valor resultante do método ainda retorna uma lista com a
# evolução da lista quando da aplicação do método.

def insere_ordenado_decrescente(lista_ordenada, elemento):
    lista_ordenada.append(elemento)  # adicionamos o elemento no fim da lista
    j = len(lista_ordenada) - 1  # índice do elemento

    while j > 0 and lista_ordenada[j - 1] < lista_ordenada[j]:
        lista_ordenada[j], lista_ordenada[j - 1] = lista_ordenada[j - 1], lista_ordenada[j]
        j -= 1


def noves_fora(lista):  # recebe uma lista de inteiros ordenada de forma decrescente
    historico_evolucao = [lista]
    nova_lista = lista
    while True:
        if len(nova_lista) == 1:
            if nova_lista[0] == 9:
                nova_lista = [0]
                historico_evolucao.append(nova_lista)
                break
            else:
                break


        soma_dois = nova_lista[0] + nova_lista[1]
        if soma_dois < 9:
            resultado = soma_dois

        else:
            if soma_dois == 9:
                resultado = 0
            else:
                resultado = soma_dois - 9
        nova_lista = []
        for i in range(2, len(historico_evolucao[len(historico_evolucao) - 1])):
            nova_lista.append(historico_evolucao[len(historico_evolucao) - 1][i])

        insere_ordenado_decrescente(nova_lista, resultado)
        if resultado != 9:
            historico_evolucao.append(nova_lista)


    resultante = nova_lista[0]


    return resultante, historico_evolucao


assert noves_fora([4]) == (4, [[4]])
assert noves_fora([9]) == (0, [[9], [0]])
assert noves_fora([9, 9]) == (0, [[9, 9], [0]])



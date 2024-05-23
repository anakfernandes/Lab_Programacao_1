def multiplica_lista(n, lista):
    multiplicacao = []

    if n == 0:
        multiplicacao = []
    else:
        i = 1
        while i <= n:
            for ele in lista:
                multiplicacao.append(ele)
            i += 1

    return multiplicacao

def multiplica_lista(n, lista):
    nova_lista = []
    for qtd_vezes in range(n):
        for elemento in lista:
            nova_lista.append(elemento)

    return nova_lista
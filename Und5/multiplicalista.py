def multiplica_lista(n, lista):
    nova_lista = []
    for qtd_vezes in range(n):
        for elemento in lista:
            nova_lista.append(elemento)

    return nova_lista
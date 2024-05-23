# Multiplica Lista

# Pede-se que você implemente a função multiplica_lista(n,lista) seguindo as especificações
# acima. Naturalmente, você não pode usar o operador de multiplicação. Além disso, a lista
# original deve manter-se inalterada após a chamada da função.
# Obs.: Lembre que se N == 0, uma lista vazia deve ser produzida.

def multiplica_lista(n, lista):
    nova_lista = []
    for i in range(n):
        for elemento in lista:
            nova_lista.append(elemento)

    return nova_lista

print(multiplica_lista(3,[0]))


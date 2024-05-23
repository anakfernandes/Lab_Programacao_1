# Encontra Menores

# Escreva a função encontra_menores(num, lista) que receba um número inteiro e uma lista
# de inteiros. A função deve retornar o primeiro valor da lista que seja menor que o
# número ou -1, se não houver valor que atenda à condição


def encontra_menores(num, lista):
    menor = -1
    for elemento in lista:
        if elemento < num:
            menor = elemento
            break

    return menor


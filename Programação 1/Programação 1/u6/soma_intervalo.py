# Soma Intervalo

# Escreva uma função soma_intervalo(a, b) que recebe dois números inteiros, a e b,
# a ≤ b, e retorna a soma dos inteiros entre a e b, inclusive. Você não deve usar a
# função sum de Python.

def soma_intervalo(a, b):
    soma = 0
    for i in range(a, b + 1):  # inclusive os dois números
        soma += i

    return soma

print(soma_intervalo(1, 11))
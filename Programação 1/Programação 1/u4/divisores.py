# Divisores Próprios

# Escreva o programa que calcula os divisores próprios de um número inteiro maior do que
# zero. Lembre que os divisores próprios de um inteiro N são todos os números menores que
# N que dividem N.

number = 12

for n in range(1, number):
    if number % n == 0:
        print(n)

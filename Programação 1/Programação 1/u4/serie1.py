# Série 1 (ranges)

# Escreva um programa que imprima todos os números da sequência abaixo. Lembre que range
# só pode representar sequências de inteiros. Logo, você precisa achar uma forma de usar
# uma iteração com range, mas imprimir os valores de ponto flutuante da sequência abaixo
# indicada:
# 8.8, 9.0, 9.2, 9.4, …, 100.0

inicio = 8.8
fim = 100.0
pulo = 0.2
repeticoes = int((fim - inicio) / pulo)

for i in range(repeticoes + 1):
    resultado = inicio + (i * pulo)
    print(f'{resultado:.1f}')
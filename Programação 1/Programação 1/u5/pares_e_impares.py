# Pares e ímpares

# Escreva um programa que leia uma sequência de inteiros da entrada até ler a palavra
# fim e que, ao final, indique quantos pares e quantos ímpares foram lidos (caso algum
# tenha sido lido)
# A entrada do programa consiste em um texto contendo N > 0 linhas com um valor inteiro
# em cada uma e uma linha adicional contendo apenas a palavra fim que é a última linha
# da entrada
# Importante: Se nenhum inteiro ímpar ou par for lido da entrada, a linha da respectiva
# contagem de ímpares ou pares não deve ser impressa na saída

pares = 0
impares = 0
while True:
    n = input()
    if n == '':
        continue

    else:
        if n == 'fim':
            break
        if int(n) % 2 == 0:
            pares += 1
        if int(n) % 2 == 1:
            impares += 1

if pares > 0:
    print(f'pares = {pares}')
if impares > 0:
    print(f'ímpares = {impares}')

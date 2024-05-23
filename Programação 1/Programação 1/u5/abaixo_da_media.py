# Abaixo da média

# Escreva um programa que dada uma sequência de valores, determina os que estão abaixo da média.

lista_valores = []
while True:
    entrada = input()
    if entrada == 'fim':
        break

    lista_valores.append(int(entrada))  # transformo cada elemento para int e adiciono na lista

soma = 0
for e in lista_valores:  # soma de todos os elementos da lista
    soma += e

media = soma / len(lista_valores)  # media de todos os elementos da lista

print(f'{media:.2f}')
# imprime os valores menores que a média dos valores lidos e a respectiva posição que o valor ocupa na sequência
for i in range(len(lista_valores)):
    if lista_valores[i] < media:
        print(i + 1, lista_valores[i])

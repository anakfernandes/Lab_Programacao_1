N = int(input())
lista_maiores = []
soma = 0

for i in range(N):
    duplas = input().split()
    if duplas[0] > duplas[1]:
        maior = duplas[0]
        lista_maiores.append(maior)
    elif duplas[0] < duplas[1]:
        maior = duplas[1]
        lista_maiores.append(maior)

for elemento in lista_maiores:
    soma += int(elemento)
    media_maiores = soma / len(lista_maiores)

if lista_maiores == []:
    print(f'Não é possível calcular a média.')
else:
    print(f'{media_maiores:.2f}')

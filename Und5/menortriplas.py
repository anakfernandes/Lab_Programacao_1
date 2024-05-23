cont = 0
menor = 0
soma = 0

media_menor = 0
maior_menor = 0
menor_menor = 0
lista_menores = []

while True:
    tripla = input().split()
    if tripla[0] == 'fim':
        break
    if tripla[0] == tripla[1] == tripla[2]:
        break
    menor = int(tripla[0])
    if menor > int(tripla[1]):
        menor = int(tripla[1])
    if menor > int(tripla[2]):
        menor = int(tripla[2])
    lista_menores.append(menor)
    cont += 1
    soma += menor
if cont > 0:
    media_menor = f'{(soma/cont):.2f}'
    maior_menor = menor_menor = lista_menores[0]
else:
    media_menor = maior_menor = menor_menor = 'nada'

for i in range(len(lista_menores)):
    if int(lista_menores[i]) < menor_menor:
        menor_menor = lista_menores[i]
    if int(lista_menores[i]) > maior_menor:
        maior_menor = lista_menores[i]

print(f'Média dos menores: {media_menor}')
print(f'Menor entre os menores: {menor_menor}')
print(f'Maior entre os menores: {maior_menor}')
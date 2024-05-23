times = input().split()  # Devem ser colocador em Ordem Alfabética
pontos = input().split()

int_pontos = []  # convertendo de str para int
for elementos in pontos:
    int_pontos.append(int(elementos))

partidas = int(input())  # número de partidas na rodada

indice_a = 0
indice_b = 0

for j in range(partidas):
    jogos = input().split()  # cada partida

    time_a = jogos[0]
    gols_a = int(jogos[1][0])

    for i in range(len(times)):  # achando o índice do time A na tabela (ordem alfabética)
        if times[i] == time_a:
            indice_a = i

    time_b = jogos[2]
    gols_b = int(jogos[1][2])

    for k in range(len(times)):  # achando o índice do time B na tabela (ordem alfabética)
        if times[k] == time_b:
            indice_b = k

    if gols_a > gols_b:  # Se o time A ganhar a partida
        int_pontos[indice_a] += 3
    elif gols_b > gols_a:  # Se o time B ganhar a partida
        int_pontos[indice_b] += 3
    else:  # Se der empate
        int_pontos[indice_a] += 1
        int_pontos[indice_b] += 1

maior = int_pontos[0]
for ponto in int_pontos:  # ponto do maior
    if ponto > maior:
        maior = ponto

menor = int_pontos[0]
for ponto in int_pontos:  # ponto do menor
    if ponto < menor:
        menor = ponto

for i in range(len(int_pontos)): # indice do maior
    if int_pontos[i] == maior:
        indice_maior = i
        break  # interrompa, quando encontrar o primeiro (ordem alfabética)

for i in range(len(int_pontos)): # indice do menor
    if int_pontos[i] == menor:
        indice_menor = i

print(f'Líder: {times[indice_maior]}')
print(f'Lanterna: {times[indice_menor]}')

# Esse código só funciano se o número de gols for menor ou igual a 9. Caso você queira
# Valores maiores, use o split('x')
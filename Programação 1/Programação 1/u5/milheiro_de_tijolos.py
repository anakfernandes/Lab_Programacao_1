# Milheiro de tijolos

# Escreva um programa que leia números da entrada que correspondem à quantidade de
# tijolos produzidos nas fornadas até que a soma dos tijolos seja maior ou igual a
# um milheiro. Ao terminar a fase de leitura de dados, deve ser produzido um relatório
# consistindo nos seguintes dados: 1) a soma total dos tijolos produzidos, 2) a média dos
# tijolos produzidos nas fornadas e 3) a quantidade de fornadas que foram acima da média.

soma_tijolos = 0  # soma total dos tijolos produzidos
cont = 0  # conta o número de fornadas
lista_tijolos = []  # contém a quantidade de tijolos de cada fornada
while True:
    tijolos_na_fornada = int(input())  # quantidade de tijolos em uma determinada fornada
    lista_tijolos.append(tijolos_na_fornada)
    soma_tijolos += tijolos_na_fornada
    cont += 1
    if soma_tijolos >= 1000:
        break

media = soma_tijolos / cont  # quantidade média de tijolos produzidos em cada fornada

acima_da_media = 0  # quantidade de fornadas que foram acima da média
for e in lista_tijolos:
    if e > media:
        acima_da_media += 1

print(soma_tijolos)
print(f'{media:.2f}')
print(acima_da_media)

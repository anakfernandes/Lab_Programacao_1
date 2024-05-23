# Imprime Ranking (Cumulativo)

n = int(input())  # número de times
# Times ordenados em ordem descrecente de pontos
times = []
pontos = []
for i in range(n):
    entrada_times = input()
    times.append(entrada_times)
    entrada_pontos = int(input())
    pontos.append(entrada_pontos)

posicao = 1
print(f'{posicao}. {times[0]} ({pontos[0]})')  # mostrando o primeiro time
for i in range(1, n):  # iteração a partir do segundo time, comparando com o anterior
    if pontos[i] != pontos[i - 1]:
        posicao = i + 1

    print(f'{posicao}. {times[i]} ({pontos[i]})')
 #camp,sc,nau,uni
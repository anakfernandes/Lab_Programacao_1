valora = int(input())
valorb = int(input())

somador = 0

for intervalo in range(valora, valorb + 1):
    if intervalo % 2 != 0:
        somador += intervalo
print(somador)

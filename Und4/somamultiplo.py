#Calcule a soma entre todos os números ímpares que são múltiplos de 3 e que estão no intervalo
#de 1 até 500

soma = 0
cont = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        cont += 1
        soma += x
print(f'A soma de todos os {cont} valores solicitados é {soma}.')





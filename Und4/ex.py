from socket import SOMAXCONN


cont = 0
soma = 0
for x in range(6):
    n = int(input())
    if n > 0:
        cont += 1
        soma += n
media = soma / cont
print(media)


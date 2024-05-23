num = int(input())
lista = input().split()

encontra_elemento = False

for elemento in lista:
    if num == int(elemento):
        encontra_elemento = True

if encontra_elemento:
    print(f'sim')
else:
    print(f'não')
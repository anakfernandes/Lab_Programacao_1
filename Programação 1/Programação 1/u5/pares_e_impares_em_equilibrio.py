# Pares e ímpares em equilíbrio

pares = []
impares = []
while True:
    n = int(input())
    if n % 2 == 0:
        pares.append(n)
    if n % 2 == 1:
        impares.append(n)
    if abs(len(pares) - len(impares)) > 2:  # se estiver em desequilíbrio, interrompa
        break

maior = len(pares)  # achando o maior
lista_maior = 'PARES'
if len(pares) < len(impares):
    maior = len(impares)
    lista_maior = 'IMPARES'

print(f'{lista_maior} em maior quantidade')
print('PARES:')

for elemento in pares:
    print(elemento)

print('IMPARES:')

for elemento in impares:
    print(elemento)

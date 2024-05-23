contador = 0
media = 0
maior = 0
numero = []

while True:
    num = int(input())
    numero.append(num)
    contador += num
    if contador >= 999: break
media = contador / len(numero)

for acima in numero:
    if acima > media:
        maior += 1

print(contador)
print(f'{media:.2f}')
print(maior)

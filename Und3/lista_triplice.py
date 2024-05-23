a = int(input())
b = int(input())
c = int(input())

votos = a + b + c

porcent_a = (a / votos) * 100
porcent_b = (b / votos) * 100
porcent_c = (c / votos) * 100

print(f'A: {a} ({porcent_a:.2f}%)')
print(f'B: {b} ({porcent_b:.2f}%)')
print(f'C: {c} ({porcent_c:.2f}%)')


if a >= b and a >= c:
    print(f'Mais votado: A')

elif b >= a and b >= c:
    print(f'Mais votado: B')

else:
    print(f'Mais votado: C')

if porcent_a > 50 or porcent_b > 50 or porcent_c > 50:
    print(f'Segundo turno: não')

else:
    print(f'Segundo turno: sim')

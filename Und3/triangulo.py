a = int(input())
b = int(input())
c = int(input())

if a < b + c and b < a + c and c < a + b:
    print(f'triangulo valido. {a + b + c}')
else:
    print(f'triangulo invalido.')
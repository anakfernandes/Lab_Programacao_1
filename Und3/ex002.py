nota1 = float(input('Qual é a sua primeira nota? '))
nota2 = float(input('Qual é a sua segunda nota? '))
nota3 = float(input('Qual é a sua terceira nota? '))

media = (nota1 + nota2 + nota3) / 3
print(f'A sua média foi {media:.1f}')

if media >= 6.0:
    print('Sua média foi boa')
else:
    print('Sua média foi ruim! Estude mais!')


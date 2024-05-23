from math import pi

print('Cálculo da Superfície de um Cilindro')
print('---')

diametro = float(input('Medida do diâmetro? '))
altura = float(input('Medida da altura? '))

areabase = ((diametro/2) **2) * pi * 2
arealateral = (diametro/2) * pi * 2 * altura

areatotal = areabase + arealateral
print('---')

print(f'Área calculada: {areatotal:.2f}')
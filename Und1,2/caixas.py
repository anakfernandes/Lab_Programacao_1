cap = float(input('Capacidade de revestimento? '))

print(f'\n== Dados do vão a revestir ==')


c = float(input('Comprimento? '))
l = float(input('Largura? '))
a = float(input('Altura? '))

area = (2 * c * l) + (2 * c * a) + (2 * l * a)

teto = c * l
areatotal = area - teto
numcaixas = int(areatotal / cap)


print(f'\n== Resultados ==')
print(f'Área total a revestir: {areatotal} m2')
print(f'Número de caixas: {numcaixas}')

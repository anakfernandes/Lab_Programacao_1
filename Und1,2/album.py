import math

totalfiguras = int(input())
qtpacote = int(input())
qtrepetidas = int(input())
valorpct = float(input())

pc = math.ceil(totalfiguras/qtrepetidas)
gasto = float(valorpct) * float(pc)
repetidas = (qtpacote - qtrepetidas) * pc

print(f'{pc}')
print(f'{repetidas}')
print('R$ {:.2f}'.format(gasto))
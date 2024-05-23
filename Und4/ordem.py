palavras = input().split()
ultima = ''
indice = 0
ordem = True

for x in palavras:
    indice += 1

    if ultima != '' and ultima > x[0]:
        ordem = False
        break
    ultima = x[0]
if ordem:
    print('em ordem')
else:
    print(f'fora de ordem: {indice}')
    
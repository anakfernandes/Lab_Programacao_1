# Movimento Uniformemente Variado

posicao_inicial = float(input('Posição inicial? '))
velocidade_inicial = float(input('Velocidade inicial? '))
tempo = float(input('Tempo? '))
aceleracao = float(input('Aceleração? '))

velocidade_final = velocidade_inicial + aceleracao * tempo
posicao_final = posicao_inicial + velocidade_inicial * tempo + (aceleracao * tempo ** 2) / 2
velocidade_media = (posicao_final - posicao_inicial) / tempo
print('')
print('Dados da questão')
print('================')

print(f'   Posição inicial: {posicao_inicial:.2f} m')
print(f'Velocidade inicial: {velocidade_inicial:.2f} m/s')
print(f'        Aceleração: {aceleracao:.2f} m/s2')
print(f'             Tempo: {tempo:.2f} s')
print(f'  Velocidade final: {velocidade_final:.2f} m/s')
print(f'  Velocidade média: {velocidade_media:.2f} m/s')
print(f'     Posição final: {posicao_final:.2f} m')

#UFCG
#ana.fernandes@ccc.ufcg.edu.br -  21.2
#solução para a questão do Bolão

placar = input()
palpites = input()

gols_A = int(placar[0])
gols_B = int(placar[2])
palpite_A = int(palpites[0])
palpite_B = int(palpites[2])

if gols_A > gols_B:      resultado_real = 'time A ganhou'
elif gols_B > gols_A:    resultado_real = 'time B ganhou'
else:                    resultado_real = 'empate'

if palpite_A > palpite_B:    resultado_palpite = 'time A ganhou'
elif palpite_B > palpite_A:  resultado_palpite = 'time B ganhou'
else:                        resultado_palpite = 'empate'

ganhou_bolao = resultado_palpite == resultado_real

if ganhou_bolao and gols_A == palpite_A and gols_B == palpite_B:
    pontos = 6
elif ganhou_bolao and (gols_A == palpite_A or gols_B == palpite_B):
    pontos = 3
elif ganhou_bolao:
    pontos = 2
else:
    pontos = 0

print(pontos)
# Acima do Limite do Elevador

razao_maxima = float(input())

crianca = 0  # número de crianças
adulto = 0  # número de adultos
peso = 0  # peso de cada pessoa
peso_total = 0
pessoas = 0  # quantidade de pessoas (adultos + crianças)
condicao = False
while True:
    entrada = input().split()
    peso = float(entrada[1])

    if entrada[0] == 'c':
        crianca += 1
        pessoas += 1
    elif entrada[0] == 'a':
        adulto += 1
        pessoas += 1
        condicao = True

    if not condicao:  # se começar com criança, interrompa
        break

    if crianca / adulto > razao_maxima or peso_total > 700:
        break

    peso_total += peso

print('Limite atingido.')
print(f'Elevador saiu com {pessoas - 1} pessoas e {peso_total:.2f} kg.')



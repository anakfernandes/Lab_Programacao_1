# Quadro de medalhas

# Faça um programa que leia as medalhas conquistadas por cada um dos dois países e
# imprima o nome do país melhor colocado no quadro de medalhas. Lembre-se: para o quadro
# de medalha, comparamos primeiro as medalhas de ouro. Quem tiver mais, é considerado o
# melhor colocado. Caso haja empate nas medalhas de ouro, comparamos as medalhas de prata.
# Caso haja empate, comparamos as de bronze.

while True:
    brasil = input().split()
    italia = input().split()

    ouro_br = 0
    ouro_ita = 0
    prata_br = 0
    prata_ita = 0
    bronze_br = 0
    bronze_ita = 0

    for elementos in brasil:  # contabilizando as medalhas do Brasil
        if elementos == '0':
            ouro_br += 1
        elif elementos == '1':
            prata_br += 1
        elif elementos == '2':
            bronze_br += 1

    for elementos in italia:  # contabilizando as medalhas da Itália
        if elementos == '0':
            ouro_ita += 1
        elif elementos == '1':
            prata_ita += 1
        elif elementos == '2':
            bronze_ita += 1

# comparando as medalhas de cada país
    if ouro_br > ouro_ita:
        print('brasil')
        break
    elif ouro_ita > ouro_br:
        print('italia')
        break
    else:
        if prata_br > prata_ita:
            print('brasil')
            break
        elif prata_ita > prata_br:
            print('italia')
            break
        else:
            if bronze_br > bronze_ita:
                print('brasil')
                break
            elif bronze_ita > bronze_br:
                print('italia')
                break
            else:
                print('empate')
                break

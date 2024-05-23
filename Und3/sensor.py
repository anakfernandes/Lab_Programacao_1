ruido = input()
hora = int(input())

if ruido == '':
    print('Condomínio em Paz.') 

else:
    if hora > 6 and hora < 22:
        print('Condomínio em Paz.')

    else: 
        print('Perturbação Detectada!')
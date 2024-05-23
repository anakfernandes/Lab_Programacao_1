tempo_ligacao = int(input())

taxa_fixa = 1

if tempo_ligacao <= 3:
    valor = tempo_ligacao * 0.50 + taxa_fixa
    print(f'R$ {valor:.2f}')


elif tempo_ligacao > 3:
    if tempo_ligacao % 5 == 0:
       
        blocos = tempo_ligacao // 5 
       
        valor = taxa_fixa + (3.00 * blocos)
        print(f'R$ {valor:.2f}')


    elif tempo_ligacao % 5 != 0:
        blocos = tempo_ligacao // 5
        extras = tempo_ligacao % 5

        valor = (blocos * 3.00) + (extras * 0.70) + taxa_fixa
        print(f'R$ {valor:.2f}')
        
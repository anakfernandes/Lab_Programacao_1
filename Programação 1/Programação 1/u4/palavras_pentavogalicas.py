# Palavras Pentavogalicas

# As palavras pentavogalicas, também chamadas panvocálicas ou pipistrelos, são palavras
# que contêm as cinco vogais (a, e, i, o, u).
# Escreva um programa que recebe uma sequencia de palavras e determina quantas delas são
# pentavogalicas.

sequencia_palavras = input(). split()

contador = 0
for palavra in sequencia_palavras:
    achou_a, achou_e, achou_i, achou_o, achou_u = False, False, False, False, False
    for letra in palavra:
        if letra == 'a':
            achou_a = True
        if letra == 'e':
            achou_e = True
        if letra == 'i':
            achou_i = True
        if letra == 'o':
            achou_o = True
        if letra == 'u':
            achou_u = True
    if achou_a and achou_e and achou_i and achou_o and achou_u:
        contador += 1

print(f'Quantidade de pentavogalicas: {contador}')

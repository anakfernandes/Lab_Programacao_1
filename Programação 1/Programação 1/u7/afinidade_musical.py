# Afinidade Musical

# A partir de duas listas de artistas que dois usuários gostam, o sistema considera que há
# afinidade musical se os dois gostam de 3 ou mais artistas iguais.
# Implemente a função tem_afinidade(l1, l2) que retorna verdadeiro caso os usuários possuam
# afinidade e falso, caso contrário.

def tem_afinidade(l1, l2):
    contador = 0

    for artista in l1:

        existencia = False  # O artista da l1 não existe na l2 até que se prove o contrário
        for i in range(len(l2)):
            if artista == l2[i]:  # Se o artista de l1 for o mesmo que algum artista da l2
                existencia = True  # O artista da l1 existe na l2
        if existencia:  # Se o artista da l1 existir na l2
            contador += 1

    if contador >= 3:  # Se existir três ou mais artistas iguais nas listas
        afinidade = True
    else:
        afinidade = False

    return afinidade


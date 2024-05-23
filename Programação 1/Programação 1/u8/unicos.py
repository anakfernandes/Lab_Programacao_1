# Únicos em comum

# Escreva a função unicos_em_comum(seq1, seq2) que retorna uma lista contendo os
# elementos únicos de seq1 que também são únicos em seq2. Caso não haja nenhum
# elemento que atenda ao critério acima, a função deve retornar uma lista vazia.

def unicos_em_comum(seq1, seq2):
    # separando os elementos que são únicos na seq1
    unicos_seq1 = []
    for elemento in seq1:
        contador = 0
        for i in range(len(seq1)):
            if elemento == seq1[i]:
                contador += 1

        if contador == 1:
            unicos_seq1.append(elemento)
    # separando os elementos que são únicos na seq2
    unicos_seq2 = []
    for elemento in seq2:
        contador = 0
        for i in range(len(seq2)):
            if elemento == seq2[i]:
                contador += 1

        if contador == 1:
            unicos_seq2.append(elemento)
    # separando os elementos únicos de seq1 que também são únicos em seq2.
    unicos = []
    for elemento in unicos_seq1:
        existe = False  # o elemento de seq1 não existe em seq2 até que se prove o contrário
        for i in range(len(unicos_seq2)):
            if elemento == unicos_seq2[i]:  # se o elemento de seq1 for o mesmo que algum elemento de seq2
                existe = True  # o elemento de seq1 existe em seq2

        if existe:  # se o elemento de seq1 existir em seq2
            unicos.append(elemento)

    return unicos










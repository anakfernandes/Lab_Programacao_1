# Diff índices

def idiff(seq1, seq2):

    maior = seq1
    menor = seq2
    if len(seq2) > len(seq1):
        maior = seq2
        menor = seq1

    diferentes = []
    for i in range(len(menor)):

        existencia = False
        if maior[i] == menor[i]:
                existencia = True

        if not existencia:
            diferentes.append(i)

    for i in range(len(menor), len(maior)):
        diferentes.append(i)


    return diferentes

seq1 = [10, 20, 30, 40, 50, 60, 70]
seq2 = [10, 20, 20, 40, 80]
assert idiff(seq1, seq2) == [2, 4, 5, 6]
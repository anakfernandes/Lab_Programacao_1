# Toppl

# Pede-se que você escreva a função filtra_alunos() que seleciona os alunos aptos a fazer
# a prova de acordo com essa condição.
# O primeiro parâmetro recebido pela função é uma lista dos alunos da disciplina com suas
# respectivas médias, na forma de uma lista de pares de matrículas e médias. O segundo é
# a lista das matrículas dos estudantes inscritos. O terceiro parâmetro é a média mínima
# necessária para estar apto a fazer o TOPPL.
# Espera-se que a função tenha efeito colateral. Ela deve alterar o conteúdo da lista de
# alunos, eliminando dela todos os alunos que não estão aptos a fazer a prova, seja por
# não ter média suficiente, seja por não terem feito a inscrição.
# A função deve ainda retornar o número de alunos que foram eliminados da lista

def filtra_alunos(alunos, inscritos, media):
    eliminados = 0
    # eliminando por média
    for i in range(len(alunos) - 1, - 1, - 1):
        if alunos[i][1] < media:
            alunos.pop(i)
            eliminados += 1
    # eliminando por inscrição
    for i in range(len(alunos) - 1, - 1, - 1):
        existe = False
        for elemento in inscritos:
            if alunos[i][0] == elemento:
                existe = True

        if not existe:
            alunos.pop(i)
            eliminados += 1

    return eliminados








inscritos = [36]
alunos = [ (120,8.0), (121,7.5), (122,5.0), (123,6.0), (124,9.0), (125,4.0), (36, 7.0) ]
assert filtra_alunos(alunos, inscritos, 7.0) == 6
assert alunos == [(36, 7.0)]

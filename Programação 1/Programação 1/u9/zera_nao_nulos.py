# Zera não-nulos!

# Pede-se que você escreva a função zera_nao_nulos(m, lin, col) que zera todos os elementos
# diferentes de zero encontrados na linha lin e na coluna col da matriz m, iniciando a
# partir da posição (lin, col). O processo de zerar é interrompido, para cada direção
# tomada a partir do início, quando um valor nulo é encontrado.

def zera_nao_nulos(m, lin, col):
    if m[lin][col] != 0:
        n_lin, n_col = len(m), len(m[0])  # número de linhas e de colunas da matriz, respectivamente

        for i in range(col, 0 - 1, - 1):  # caminhando pela esquerda
            if m[lin][i] == 0:
                break
            m[lin][i] = 0

        for i in range(col + 1, n_col):  # caminhando pela direita
            if m[lin][i] == 0:
                break
            m[lin][i] = 0

        for i in range(lin - 1, 0 - 1, - 1):  # caminhando para cima
            if m[i][col] == 0:
                break
            m[i][col] = 0

        for i in range(lin + 1, n_lin):  # caminhando para baixo
            if m[i][col] == 0:
                break
            m[i][col] = 0

jogo = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
       ]

zera_nao_nulos(jogo, 3, 5)

assert jogo == [
        [1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 0],
       ]


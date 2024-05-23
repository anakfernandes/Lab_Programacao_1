# Matriz Coincidência

# Escreva a função matriz_coincidencia(M1, M2) que receba duas matrizes e identifique as
# coincidências entre elas, ou seja, elementos que se encontram na mesma posição (linha e
# coluna). A função deve retornar uma nova matriz contendo os elementos que coincidem nas
# suas posições e 0 (zero) nas demais posições. Todas as matrizes recebidas pela função e
# a matriz retornada devem ter o mesmo número de linhas e colunas. Não haverá matrizes vazias.
def cria_matriz_vazia(n_lin, n_col):
    result = []
    for i_lin in range(n_lin):
        linha = []
        for i_col in range(n_col):
            linha.append(None)
        result.append(linha)

    return result


def matriz_coincidencia(M1, M2):
    n_lin, n_col = len(M1), len(M1[0])  # número de linhas e de colunas das matrizes
    # criar a estrutura
    result = cria_matriz_vazia(n_lin, n_col)
    # popular a estrutura
    for i_col in range(n_col):
        for i_lin in range(n_lin):
            if M1[i_lin][i_col] == M2[i_lin][i_col]:
                result[i_lin][i_col] = M1[i_lin][i_col]
            else:
                result[i_lin][i_col] = 0

    return result


M1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

M2 = [[10, 11, 12], [13, 14, 15], [7, 8, 9]]

M3 = [[1, 2, 3], [13, 14, 15], [16, 17, 18]]

print(matriz_coincidencia(M1, M2))
print(matriz_coincidencia(M1, M3))

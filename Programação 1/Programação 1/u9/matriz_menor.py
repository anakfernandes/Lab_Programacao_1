# Matriz Menor

# Escreva uma função que receba duas matrizes de números inteiros e verifica entre os
# elementos que se encontram na mesma posição (linha e coluna) quem dos dois é o menor.
# A função deve retornar uma nova matriz composta pelos menores números encontrados em
# suas respectivas posições. Todas as matrizes recebidas pela função e a matriz retornada
# devem ter o mesmo número de linhas e colunas. Não haverá matrizes vazias

def cria_matriz_vazia(n_lin, n_col):
    result = []
    for i_lin in range(n_lin):
        linha = []
        for i_col in range(n_col):
            linha.append(None)
        result.append(linha)

    return result


def matriz_menor(M1, M2):
    n_lin, n_col = len(M1), len(M1[0])  # número de linhas e de colunas da matriz, respectivamente
    # criar a estrutura
    result = cria_matriz_vazia(n_lin, n_col)
    # popular a estrutura
    for i_lin in range(n_lin):
        for i_col in range(n_col):
            menor = M1[i_lin][i_col]
            if M2[i_lin][i_col] < menor:
                menor = M2[i_lin][i_col]
            result[i_lin][i_col] = menor

    return result


M1 = [[1,2,3],[13,14,15],[7,8,9]]

M2= [[10,11,12],[4,5,6],[7,8,9]]

M3= [[1,2,3],[0,0,0],[7,8,9]]

assert matriz_menor(M1, M2) == [[1,2,3],[4,5,6],[7,8,9]]
assert matriz_menor(M1, M3) == [[1,2,3],[0,0,0],[7,8,9]]

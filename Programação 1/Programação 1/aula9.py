def cria_matriz_vazia(n_lin, n_col):
    result = []
    for i_lin in range(n_lin):
        linha = []
        for i_col in range(n_col):
            linha.append(None)
        result.append(linha)

    return result

def dobra_valores(matriz):
    n_lin, n_col = len(matriz), len(matriz[0])  # número de linhas e de colunas da matriz, respectivamente
    # criar a estrutura
    result = cria_matriz_vazia(n_lin, n_col)
    # popular a estrutura
    for i_col in range(n_col):
        for i_lin in range(n_lin):
            result[i_lin][i_col] = 2 * matriz[i_lin][i_col]

    return result


dados = [[10, 5, 2],
         [2, -1, 3],
         ]

print(dobra_valores(dados))


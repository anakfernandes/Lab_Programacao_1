# Diagonais

# Escreva a função diagonais(M) que retorna uma matriz cuja primeira linha contem os
# valores da diagonal principal de M, enquanto a segunda linha contém os valores da
# diagonal secundária de M, sendo M uma matriz quadrada.

def diagonais(M):
    principal = []
    secundaria = []
    result = []
    n_lin, n_col = len(M), len(M[0])  # número de linhas e de colunas da matriz, respectivamente
    # achando a diagonal principal e a secundária
    k_col = n_col - 1
    for i_lin in range(n_lin):
        principal.append(M[i_lin][i_lin])
        secundaria.append(M[i_lin][k_col])
        k_col -= 1

    result.append(principal)
    result.append(secundaria)

    return result


M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

M1 = [[1, 2],
      [3, 4]]

M3 = [[1]]

assert diagonais(M) == [[1, 5, 9], [3, 5, 7]]
assert diagonais(M1) == [[1, 4], [2, 3]]
print(diagonais(M3))
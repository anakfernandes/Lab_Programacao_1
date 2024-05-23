# Scroll

# Pede-se que você escreva a função scroll(m) que recebe uma matriz m e que a altera
# movendo todos os seus dados uma linha acima. Os dados da última linha, contudo, devem
# ser todos zerados.

def scroll(m):
    n_lin, n_col = len(m), len(m[0])  # número de linhas e de colunas da matriz, respectivamente
    for i_lin in range(n_lin):
        for i_col in range(n_col):
            if i_lin == n_lin - 1:
                m[i_lin][i_col] = 0
            else:
                m[i_lin][i_col] = m[i_lin + 1][i_col]



m = [[1,  2,  3,  4], [4, 5 ,6 ,5]]

scroll(m)
assert m == [ [4,5,6,5],[  0,  0,  0,  0 ]]

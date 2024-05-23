# Quantos Comeram?

# Dona Inês sempre prepara apenas feijoada suficiente para N pessoas. A demanda, contudo,
# é tipicamente maior ou igual ao que ela preparou. Quando a feijoada não é capaz de ser-
# vir todos os alunos de um grupo, todos os alunos do grupo desistem de comer feijoada.
# Mesmo com feijoadas sobrando, Dona Inês também para de servir feijoadas depois que o
# primeiro grupo de alunos desistir de comer em sua cantina.

# Pede-se que você escreva a função quantos_comeram(N, fila_pedidos) que recebe a quanti-
# dade N de feijoadas feitas por Dona Inês, e uma representação da fila de grupos de pedi-
# dos (cada valor na fila indica quantas feijoadas aquele grupo pediu), e que retorne quan-
# tas feijoadas foram, de fato, consumidas no dia.

def quantos_comeram(N, fila_pedidos):
    consumo = 0  # feijoadas consumidas
    for valor in fila_pedidos:
        consumo += valor
        if consumo > N:
            consumo -= valor
            break

    return consumo


assert quantos_comeram(10, [10, 10]) == 10
assert quantos_comeram(12, [10, 10]) == 10
assert quantos_comeram(2, [10, 10]) == 0
assert quantos_comeram(2, [2]) == 2
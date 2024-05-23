# UFCG
# ana.fernandes@ccc.ufcg.edu.br Turma: 21.2
# Solução Pedidos de carros

def pedidos_carros(num, pedidos):
    num_aceitos = 0
    for i in range(len(pedidos)):
        if pedidos[i] <= num:
            num_aceitos += pedidos[i]
            num -= pedidos[i]
    return num_aceitos
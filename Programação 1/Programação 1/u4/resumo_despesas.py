# Título: Resumo das despesas

# Implemente um programa que, dado o registro de compras de um cartão de crédito, imprima
# a soma de gastos de uma determinada categoria.

numero_registros = int(input())

categoria = []
gasto = []
for i in range(numero_registros):
    registros = input().split(',')  # categoria,gasto
    categoria.append(registros[0])
    gasto.append(registros[1])

categoria_usuario = input()  # categoria que o usuário deseja ver a soma dos gastos

soma = 0
for i in range(len(categoria)):
    if categoria[i] == categoria_usuario:
        soma += int(gasto[i])
print(f'R$ {soma}')


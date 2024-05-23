adultos = int(input())
criancas = int(input())
preco = float(input())

preco = (adultos*preco + criancas/2 *preco)
print(f'Total: R$ {preco:.2f}')
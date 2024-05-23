soma = 0
quant_produtos = 0
lista_valores = []

while True:
	valor_produto = input()
	if valor_produto == "fim":	break
	soma += float(valor_produto)
	quant_produtos += 1
	lista_valores.append(float(valor_produto))

media = soma / quant_produtos
maior_valor = 0

for x in range(len(lista_valores)):
	if lista_valores[x] > maior_valor:
		maior_valor = lista_valores[x]

print (f"O valor médio por produto foi R$ {media:.2f}. O produto mais caro custa R$ {maior_valor:.2f}")


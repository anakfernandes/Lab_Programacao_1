N = int(input())

categorias = []
valor = []
for i in range(N):
    entrada = input().split(',')
    categorias.append(entrada[0])
    valor.append(entrada[1])

tipo = input()  

soma = 0
for i in range(len(categorias)):
    if tipo == categorias[i]:
        soma += int(valor[i])

print(f'R$ {soma}')

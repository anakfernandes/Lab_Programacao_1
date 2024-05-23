# Desenhando uma Árvore de Natal

# Escreva um programa que desenha uma arvore de natal em forma de um triangulo de letras
# o e uma letra o para representar o tronco.

altura = int(input())  # altura do triângulo
simbolo = 'o'
largura_inicio = altura - 1

largura_variavel = largura_inicio
for i in range(altura):
    if largura_variavel > 0:
        print(f"{' ' * (largura_variavel)}{simbolo}")
    else:
        print(simbolo)

    simbolo += 'oo'
    largura_variavel -= 1
print(f"{' ' * largura_inicio}{'o'}")  # tronco

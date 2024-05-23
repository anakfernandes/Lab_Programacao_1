# Fora de ordem

# Escreva um programa que recebe uma dada sequência de palavras e verifica se a sequência
# recebida está em ordem alfabética.
# caso esteja fora de ordem, indicar a posição da primeira palavra fora de ordem.
palavras = 'caso dado abacate tatu'.split()
posicao = 0
ordenado = True  # A lista está ordenada até que se prove o contrário
for i in range(len(palavras) - 1):  # Na última iteração, comparamos a penúltima palavra com a última
    if palavras[i] > palavras[i + 1]:  # Analisando se palavras[i] vem depois de palavras[i + 1]
        ordenado = False
        posicao = i + 2
        break

if ordenado:
    print("em ordem")
else:
    print(f"fora de ordem: {posicao}")



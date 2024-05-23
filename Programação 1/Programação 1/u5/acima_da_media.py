# Acima da média

media_spp = float(input())  # o valor da média mensal estabelecida pela ssp

lista = []
while True:
    entrada = input()  # a quantidade de ocorrências registradas por dia na delegacia (sequência)
    valores = entrada.split()

    if entrada == 'fim':
        break

    for i in range(len(valores)):  # convertendo de str para int
        valores[i] = int(valores[i])

    soma = 0
    for valor in valores:  # somando cada valor da lista
        soma += valor

    media_valores = soma / len(valores)

    if media_valores > media_spp:  # cada elemento da lista será a sequência de valores
        lista.append(entrada)      # da entrada maiores que a média

    if media_valores < (media_spp / 2):
        break
# imprimir na saída apenas as sequências cuja média mensal é maior que o estabelecido.
for elemento in lista:
    print(elemento)

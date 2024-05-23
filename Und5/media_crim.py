media_dept = float(input())
soma = 0
lista_maior = []
while True:
    entrada = input()
    if entrada == 'fim': break
    valores = entrada.split()
    soma = 0
    for valor in valores:
        soma += float(valor)

    media_valores = soma / len(valores)

    if media_valores * 2 < media_dept: break

    if media_valores > media_dept:
        lista_maior.append(entrada)

for lista in lista_maior:
    print(lista)
# Título: Tiro ao Alvo

# A entrada do programa consiste em uma sequência de N > 1 pares de números indicando
# posições no plano em que os disparos foram feitos. Cada par é lido em uma linha da
# entrada, com os valores separados por espaços. O fim da entrada é caracterizado por
# um disparo feito a mais de 200 centímetros do centro do alvo.

acumulador_distancia = 0
contador = 0

while True:
    plano = input().split()
    x = float(plano[0])
    y = float(plano[1])
    distancia = (x ** 2 + y ** 2) ** (1/2)

    if distancia > 200:
        break

    print(f"{distancia:.2f}cm")
    acumulador_distancia += distancia
    contador += 1

distancia_media = acumulador_distancia / contador
print("--")
print(f"num disparos: {contador}")
print(f"distancia media: {distancia_media:.2f}cm")

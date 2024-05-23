import math

raio = float(input())
voltas = float(input())

distancia = (math.pi * raio * 2) * voltas

print(f'A pessoa percorreu {distancia:.3f} metros')
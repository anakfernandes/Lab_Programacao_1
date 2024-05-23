# Vagoes

# Escreva um programa que recebe uma lista de inteiros que
# representa a quantidade de peças acondicionadas em cada um dos
# vagões e um valor inteiro K que define um valor limite para
# que vagões adjacentes estejam balanceados. O programa deve
# determinar quantos vezes a diferença absoluta entre quantidades
# de peças de vagões vizinhos é maior do que K.

k = 1  # Valor limite para que vagoes adjacentes estejam balanceados
pecas_vagao = '20'.split()

int_pecas_vagao = []
for i in range(len(pecas_vagao)):  # Transformando pecas_vagao em uma lista de inteiros
    int_pecas_vagao.append(int(pecas_vagao[i]))

desbalanceamento = 0
for i in range(len(int_pecas_vagao) - 1):
    if abs(int_pecas_vagao[i + 1] - int_pecas_vagao[i]) > k:
        desbalanceamento += 1

print(desbalanceamento)  # o número de pares de vagões adjacentes desbalanceados(cuja diferença absoluta é maior do que K)



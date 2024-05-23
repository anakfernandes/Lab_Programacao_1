# Adiciona Maior Diferença Entre Vizinhos

# Escreva a função adiciona_maior(lista) que modifica a lista de inteiros recebida como
# parametro, adicionando a cada elemento da lista o valor da maior diferença absoluta
# entre dois elementos vizinhos da lista

def adiciona_maior(lista):

    maior_diferenca = 0
    for i in range(len(lista) - 1):
        if abs(lista[i] - lista[i + 1]) > maior_diferenca:
            maior_diferenca = abs(lista[i] - lista[i +1])

    for i in range(len(lista)):
        lista[i] += maior_diferenca






l1 = [2, 6, 5, 4, 0, 1]
assert adiciona_maior(l1) == None
assert l1 == [6, 10, 9, 8, 4, 5]
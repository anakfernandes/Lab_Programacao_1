# Vacina Idosos Primeiro

# Como o sistema armazenou os dados na ordem em que os mesmos foram cadastrados, não há
# nenhuma priorização. Contudo, devemos considerar que quem possui 60 anos ou mais deve
# tomar a vacina primeiro.
# Sendo assim, você deve criar a função vacina_idosos(lista) que, dada uma lista das idades
# das pessoas cadastradas (ordenada segundo a ordem de cadastro no sistema), altera a lista
# da seguinte forma: o primeiro idoso encontrado na lista deve ser movido para a primeira
# posição da lista, o segundo idoso deve ser movido para o segundo da fila, e assim por
# diante.

def vacina_idosos(fila):  # recebe uma lista como parâmetro
    for j in range(len(fila) - 1):
        encontrei_idoso = False
        indice_idoso = j  # O índice do mínimo começa assumindo o índice da posição mínima disponível (o j é o ponto de início das posições disponíveis no momento)
        for i in range(j, len(fila)):
            if fila[i] >= 60:  # Se encontrar um idoso
                indice_idoso = i
                encontrei_idoso = True
                break
        if encontrei_idoso:  # mova o idoso para a posição mínima diponível
            for i in range(indice_idoso, j, -1):
                fila[i], fila[i - 1] = fila[i - 1], fila[i]

fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
vacina_idosos(fila)
print(fila)
assert fila == [67, 61, 63, 75, 25, 33, 35, 8, 12, 15, 22, 30, 34]
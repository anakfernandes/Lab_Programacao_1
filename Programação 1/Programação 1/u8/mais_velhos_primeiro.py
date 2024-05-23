# Mais Velhos Primeiro

# Pede-se que você implemente uma função que, dada uma lista das idades dos passageiros
# (ordenada segundo a fila de embarque), altere a lista da seguinte forma: o primeiro idoso
# encontrado na lista deve trocar de posição com o primeiro da fila, o segundo idoso deve
# trocar de posição com o segundo da fila, e assim por diante. Considere que idosos são
# pessoas com 60 anos ou mais.

def idosos_inicio(fila):  # recebe uma lista como parâmetro
    for j in range(len(fila) - 1):
        encontrei_idoso = False
        indice_idoso = j  # O índice do mínimo começa assumindo o índice da posição mínima disponível (o j é o ponto de início das posições disponíveis no momento)
        for i in range(j, len(fila)):
            if fila[i] >= 60:  # Se encontrar um idoso
                indice_idoso = i
                encontrei_idoso = True
                break
        if encontrei_idoso:  # troque o idoso com quem estiver na posição mínima diponível
            fila[j], fila[indice_idoso] = fila[indice_idoso], fila[j]










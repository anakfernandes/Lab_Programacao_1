def selection_sort(lista):
    for j in range(len(lista) - 1):  # O j só precisa ir até a penúltima posição
        min_index = j  # O índice do mínimo começa assumindo o índice posição mínima disponível (o j é o ponto de início das posições disponíveis no momento
        for i in range(j, len(lista)):
            if lista[i] < lista[min_index]:
                min_index = i  # índice do mínimo
        if lista[j] > lista[min_index]:  # Se quem está na posição miníma disponível,for maior que o mínimo, troque-os de posição
            auxiliar = lista[j]  # a variável auxiliar guarda o valor de lista[j]
            lista[j] = lista[min_index]  # coloque na posição j o valor que estava na posição de índice mínimo
            lista[min_index] = auxiliar

def insere_ordenado(lista_ordenada, elemento):
    lista_ordenada.append(elemento)
    j = len(lista_ordenada) - 1  # índice do novo elemento

    while j > 0 and lista_ordenada[j - 1] > lista_ordenada[j]:
        lista_ordenada[j], lista_ordenada[j - 1] = lista_ordenada[j - 1], lista_ordenada[j]
        j -= 1  # quando o elemento troca de posição, ele assume o índice do seu vizinho da esquerda

#  Primeiro, adicionamos o elemento no fim da lista_ordenada, por meio do append()
#  Segundo, comparamos ele com o vizinho da esquerda. Caso o elemento seja menor que o
#  vizinho da esquerda, troque.
# Critérios de parada:
#  Se o vizinho da esquerda for menor ou igual a ele, ele para. Isso ocorre, pois ele não precisa
# testar o restante, visto que a lista está ordenada.
# Se o elemento estiver no índice 0 ele para também, pois isso significa que ele já é
# o menor elemento e não há vizinhos da esquerda para se comparar.

def merge(lista1, lista2):
    lista3 = []
    i = 0  # caminhar em lista1
    j = 0  # caminhar em lista2

    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            lista3.append(lista1[i])
            i += 1
        else:
            lista3.append(lista2[j])
            j += 1
    # descobrindo a lista que chegou no final
    if i == len(lista1):
        lista3 += lista2[j:]
    else:
        lista3 += lista1[i:]

    return lista3


# Na primeira iteração do While será comparado o primeiro elemento de cada lista, o menor
# deles será adicionado à lista3. Nas próximas iterações, continuará sendo comparado os
# menores de cada lista.

# Quando uma das listas chegar ao final, significa que eu não preciso mais comparar uma
# lista com a outra. Logo, o que sobrou da outra lista, eu preciso adicionar a lista3
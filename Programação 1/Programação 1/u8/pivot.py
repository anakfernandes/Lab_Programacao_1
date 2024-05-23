# Pivot

def pivot(numeros):
    vetor = numeros[0]

    existe = False
    indice = 0
    for i in range(len(numeros)):
        if numeros[i] < vetor:
            indice = i
            existe = True
            break

    if existe:
        for j in range(len(numeros) - 1):  # Se fizermos o procedimento abaixo len(lista) - 1 com certeza teremos uma lista ordenada no final
            for i in range(indice , 0, - 1):
                if numeros[i - 1] == vetor :  # se o elemento da direita for menor que o elemento da esquerda
                    numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]  # troque-os de lugar
                    break
                numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]

lista = [6, 5,8 ,7 ,3, 1,2, 10]
pivot(lista)
print(lista)
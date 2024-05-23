lista = [1, 2, 3, 4, 5]
lista1 = [18, 19, 20, 100]
lista2 = [18, 20, 19, 50, 50, 94]
# FOR para somar os elementos da lista com seu vizinho:

for i in range(len(lista) -1):
    lista[i] += lista[i + 1]
print(lista)

# FOR para somar todos os elementos da lista:
soma = 0

for elemento in range(len(lista)):
    soma += int(lista[elemento])
print(soma)

# FOR para decrementar os elementos da lista:

for elemento in range(len(lista) -1):
    if i != 0 and lista[i - 1] == lista[i]:
        lista[i] -= 1

for i in range(len(lista)):
    if lista1[i] == lista2[i]:
        if lista[i + 1] == lista[i + 1]:
            if lista[i + 2] == lista[i + 2]:
                faca = lista[i]

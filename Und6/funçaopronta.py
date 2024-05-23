# if ... in
def meu_in(lista, elemento):
    for e in lista:
        if e == elemento:
            return True
    return False

# sum()
def soma(lista):
    s = 0
    for i in lista:  
        s += i
    return s

# frase.split('*')
def split(frase, delimitador):
    str_vazia = ''
    splitted = []
    for letra in frase:
        if letra != delimitador:
            str_vazia += letra
        else:
            if str_vazia == '':
                str_vazia = '' 
            else:
                splitted.append(str_vazia)
                str_vazia = ''
    if str_vazia:
        splitted.append(str_vazia)
    return splitted

# palavra.join('')
def meu_join(delimitador, sequencia_de_string):
    assert len(sequencia_de_string) > 0
    joinfinal = ''    
    for i in range(len(sequencia_de_string)):
        if i < len(sequencia_de_string) - 1:
            joinfinal += f'{sequencia_de_string[i]}{delimitador}'
        else:
            joinfinal += str(sequencia_de_string[i])
    return joinfinal

# insere na lista
def meu_insert(lista, indice, elemento):
    nova_lista = []
    for i in range(len(lista)):
        if indice == i:
            auxiliar = lista[indice]
            lista[indice] = elemento
            nova_lista.append(lista[indice])
            nova_lista.append(auxiliar)
        else:
            nova_lista.append(lista[i])

    return nova_lista

# slice()
def meu_slice(lista, começo, fim):
    listanova = []
    for i in range(começo, fim):
        listanova.append(lista[i])
    
    return listanova

# sort() / bubblesort
def ordem_decrescente(lista):
    tamanho = len(lista)
    listanova = []
    while len(listanova) < tamanho:
        maior = lista[0]
        ind = 0
        for i in range(len(lista)):
            if lista[i] > maior:
                maior = lista[i]
                ind = i
        lista.pop(ind)
        listanova.append(maior)
    return listanova

# remove()
def meu_remove(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            lista.pop(i)
            break
    return lista

# remove elementos iguais da lista
def remove_iguais(lista, elemento):
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == elemento:
            lista.pop(i)
    return lista

# lista1 + lista2
def meu_extend(lista1, lista2):
    for i in lista2:
        lista1.append(i)
    return lista1

# troca 2 valores - ex: x = 1 e y = 2 --> x = 2 e y = 1
def swap(lista, i, k):
    auxiliar = lista[i]
    lista[i] = lista[k]
    lista[k] = auxiliar

# copy()
def copy(lista):
    lista_copia = []
    for i in lista:
        lista_copia.append(i)
    return lista_copia

# slice(start, stop, step)
def meu_slice(lista, começo, fim):
    listanova = []
    for i in range(começo, fim):
        listanova.append(lista[i])
    
    return listanova
    
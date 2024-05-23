print('TIPOS DE LAÇO FOR\n')

# Input com espaços + Criar lista de strings
entrada = input().split()
print('Lista = ', entrada)

print('\n== Cada índice ==')

## FOR DE VALORES ##
for i in entrada:
    print(i)        # imprime cada indice de entrada

print('\n== Tem essa fruta? ==')

# Ex 1 - For de Valores
lista = ['banana', 'maça', 'melancia']
# Para cada elemento em 'entrada'...
for elemento in entrada:
    # Pegue cada fruta da 'lista'
    for fruta in lista:
        # Se a fruta for igual ao elemento da entrada
        if fruta == elemento:
            print(f'Tem {fruta} aqui!')

print('\n== N de caracteres ==')

## FOR POR INDICE ##
# Uso range(len()) para transformar em inteiro

# FOR APENAS COM UM VALOR = quantas vezes eu quero que o laço seja executado
palavra = 'for'
       # Pegue o número de letras (caracteres) de palavra
for i in range(len(palavra)):
    print('estudando...')

print('\n== Onde começar ==')

# FOR DE DOIS VALORES
# range(start, end)
nome = 'onibus'
       # Comece no indice [3]
for i in range(3, len(nome)):
    print(nome[i])              # imprimir cada indice de 'nome'

print('\n== Pular índices ==')

# FOR COM TRÊS VALORES
variavel = 'mensagem-secreta'
# range(start, end, delta)  delta --> pular de quanto em quanto
for i in range(2, len(variavel), 3):
    print(variavel[i])

# FOR QUE PERCORRE DE TRÁS PARA FRENTE
palavra = 'aluno'

print('\n=== Caso 1 ===')
# Apenas remove o último indice: comparar [i] e [i + 1] por exemplo
for i in range(len(palavra) - 1):
    print(palavra[i])

print('\n=== Caso 2 ===')
# Percorre de trás para frente
for i in range(len(palavra) - 1, -1, -1):
    print(palavra[i])

print('\n== Índice dentro de índice ==')

# LAÇOS ANINHADOS
frase = 'os fins justificam os meios'.split()
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# no indice[4] = meios
print(frase[4][3]) # pegue o caractere[3] = o

# no indice[2] = [7, 8, 9]
print(lista[2][1]) # pegue o indice[1] = 8

print('\n== Adicionar na lista ==')

novalista = []
for sublista in lista:
    for num in sublista:
        novalista.append(num)

print(novalista)

print('\n== RESUMO ==')

for palavra in frase:
    for letra in palavra:
        print(letra)

print('\nou...\n')

# Pegue cada palavra da frase
for palavra in frase:
               # len(Pegue o tamanho da palavra)
    for letra in range(len(palavra)): # range(E transforme num número)
      # Imprima cada indice de letra de palavra
        print(palavra[letra])

print('\nou...\n')

# i = indice
# Pegue o tamanho da frase
for i in range(len(frase)):
    # Pegue cada letra do indice de frase
    for letra in frase[i]:
        print(letra)
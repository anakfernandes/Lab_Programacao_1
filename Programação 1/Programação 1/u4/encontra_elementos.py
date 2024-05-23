numero = int(input())  # o número N que deve ser procurado na lista de inteiros
lista = input().split()  # a sequência de inteiros onde a busca deve ser feita

encontrou = False  # nenhum número foi encontrado até que se prove o contrário
for elemento in lista:
    if numero == int(elemento):
        encontrou = True  # o número foi encontrado

if encontrou:  # caso o número tenha sido encontrado na lista
    print('sim')
else:
    print('não')

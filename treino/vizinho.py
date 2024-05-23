N = int(input())

lista_nums = []
vizinhos = ''

for i in range(N):
    numeros = int(input())
    lista_nums.append(numeros)

for i in range(len(lista_nums) -1):
    if int(lista_nums[i]) == int(lista_nums[i + 1]):
        lista_nums[i + 1] -= 1

for i in range(len(lista_nums)):
    if i == len((lista_nums) -1):
        vizinhos += str(lista_nums[i])
    else:
        vizinhos += str(lista_nums[i]) + ' '

print(f'{vizinhos}')

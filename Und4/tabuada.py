#Mostre a tabuada do número que o usuário digitar utilizando o laço for

num = int(input('Digite um número para ver sua tabuada: '))
for x in range(1, 11):
    print(f'{num} x {x} = {num * x}')
    


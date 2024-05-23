cpf1 = int(input())
cpf2 = int(input())
cpf3 = int(input())

cpf11 = cpf1 // 100
cpf22 = cpf2 // 100
cpf33 = cpf3 // 100

cpf111 = cpf1 % 100
cpf222 = cpf2 % 100
cpf333 = cpf3 % 100

cpf1111 = (cpf1 // 1) % 10 + (cpf1 // 10) % 10
cpf2222 = (cpf2 // 1) % 10 + (cpf2 // 10) % 10
cpf3333 = (cpf3 // 1) % 10 + (cpf3 // 10) % 10

print(f"{cpf11}-{cpf111}")
print(f'{cpf1111}')
print(f"{cpf22}-{cpf222}")
print(f'{cpf2222}')
print(f"{cpf33}-{cpf333}")
print(f'{cpf3333}')

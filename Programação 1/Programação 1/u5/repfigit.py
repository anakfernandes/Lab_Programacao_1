# Repfigit

num = input()
t0 = int(num[0])
t1 = int(num[1])

print(t0)
print(t1)

sequencia = [t0, t1]
i = 0  # índice do número
elemento = 0
while True:
    elemento = sequencia[i] + sequencia[i + 1]  # soma o numero com seu vizinho da direita
    if elemento > int(num):
        break
    sequencia.append(elemento)
    print(elemento)
    i += 1

print('---')

if sequencia[len(sequencia) - 1] == int(num):  # observando se o último elemento da lista é igual a num
    print(f'{num} é um repfigit.')
else:
    print(f'{num} não é um repfigit.')

#UFCG
#ana.fernandes@ccc.ufcg.edu.br
#Solução Equações válidas

while True:
    a = float(input('a? '))
    b = float(input('b? '))
    c = float(input('c? '))
    delta = (b ** 2) - 4 * a * c
    if a == 0 or delta <= 0:
        print('equação inválida: tente novamente')
    else:  
        break

x1 = (- b + delta ** (1/2)) / (2 * a)
x2 = (- b - delta ** (1/2)) / (2 * a)

print(f'{x1:.3f}')
print(f'{x2:.3f}')
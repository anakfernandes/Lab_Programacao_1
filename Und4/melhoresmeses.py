soma = 0
media = 0
meses = []
for i in range(12):
    num = int(input())
    meses.append(num)
    soma += num
media = soma / 12
print(f'média = {media:.2f}')

print('--- acima da média')
for i in range(len(meses)):
    if media < meses[i]:
        print(f'mês {i+1}: {meses[i]}')

print('--- abaixo da média')
for i in range(len(meses)):
    if media > meses[i]:
        print(f'mês {i+1}: {meses[i]}')
        

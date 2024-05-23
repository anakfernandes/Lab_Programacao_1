xi = int(input())
yi = int(input())
xj = int(input())
yj = int(input())
xk = int(input())
yk = int(input())

didj = (((xi - xj) ** 2) + (((yi - yj)) ** 2)) ** 0.5
djdk = (((xj - xk) ** 2) + (((yj - yk)) ** 2)) ** 0.5
dkdi = (((xk - xi) ** 2) + (((yk - yi)) ** 2)) ** 0.5

perimetro = didj + djdk + dkdi

print(f'O perímetro é de {perimetro:.2f}') 
a = float(input())
b = float(input())
c = float(input())

delta = (b ** 2) - (4 * a * c)

if delta < 0:
	print('sem raizes reais')

else:
	x1 = (-b + delta ** 0.5) / (2 * a)
	x2 = (-b - delta ** 0.5) / (2 * a)
	if x1 == x2:
		print(f'x = {x1:.2f}')
	else:
		print(f'x1 = {x1:.2f}')
		print(f'x2 = {x2:.2f}')
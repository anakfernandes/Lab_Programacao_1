limite = int(input())
i = 1
soma = 0

while soma < limite:
	soma += i
	if soma > limite: break
	if soma < limite:
		print(i)
	i += i	
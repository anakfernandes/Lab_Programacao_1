print "Mastery Learning"
print "Cálculo da nota na unidade"

while True:
	nota_1 = float(input("Nota? "))
	nota_2 = float(input("Nota? "))
	media = (nota_1 + nota_2) / 2
	if media >= 7.0: break
	print (f'Média: {media:.1f}')
    

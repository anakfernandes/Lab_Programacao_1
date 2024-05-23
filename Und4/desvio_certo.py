def media(numeros):       
    soma = 0
    for n in numeros:
        soma += n       
    media = soma / len(numeros)
    return media 

lista1 = [1, 1, 1.2, 1, 1, 1.1, 2]
lista2 = [2, 3, 4, 5, 6]
soma_quadrado1 = 0
soma_quadrado2 = 0

for elemento in range(len(lista1)):    
    diferenca1 = float(lista1[elemento]) - media(lista1) 
    quadrado_dif = diferenca1 ** 2 
    soma_quadrado1 += quadrado_dif 
    diferenca1 = soma_quadrado1 / (len(lista1) - 1) 
    desvio1 = diferenca1  ** ( 1 / 2 )

for elemento in range(len(lista2)):    
    diferenca2 = float(lista2[elemento]) - media(lista2) 
    quadrado_dif = diferenca2 ** 2 
    soma_quadrado2 += quadrado_dif 
    diferenca2 = soma_quadrado2 / (len(lista2) - 1) 
    desvio2 = diferenca2  ** ( 1 / 2 )

if desvio1 > desvio2:
    seq_maior = 1
elif desvio2 > desvio1:
    seq_maior = 2
else:
    print(f'As sequências possuem o mesmo desvio padrão ({desvio1:.2f})')

print(f'A sequência {seq_maior} possui o maior desvio padrão ({desvio1:.2f})')
def impares(numeros): #inicio
    impares = []
    for n in numeros:    #corpo da função ou hora do laço
        if n % 2 == 1:
            impares.append() 
    return impares            #resultado

           
def maximo(numeros):    
    maximo = numeros[0]   
    for n in numeros:
        if n > maximo:
            maximo = n 
    return maximo           


def media(numeros):       
    soma = 0
    for n in numeros:
        soma += n       
    media = soma / len(numeros)
    return media   

numeros = [2,7,8,3,4,5,6,10,15,17]
print(maximo(numeros))
print(media(numeros))
print(impares(numeros))
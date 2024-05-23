# Quase sílabas

# Programa que identifique todos os pares de letras vizinhas de palavras em que a primeiro
# seja consoante e a segunda seja uma vogal.
# Pede-se que você escreva a função quase_fonemas(palavra) que retorna uma lista contendo
# os possíveis fonemas de acordo com a especificação dada pelo estudante. Ou seja, a lista
# deve conter strings que correspondem a pares de letras vizinhas em que a primeira é uma
# consoante e a segunda é uma vogal

def quase_fonemas(palavra):

    fonemas = []
    for i in range(1, len(palavra)):
        if palavra[i] in 'aeiou':
            if palavra[i - 1] not in 'aeiou':
                par = palavra[i - 1] + palavra[i]
                fonemas.append(par)

    return fonemas




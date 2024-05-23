# Vogais Primeiro

# Escreva a função vogais_primeiro(frase) que recebe a string frase e retorna outra
# string contendo exatamente os mesmos caracteres, na mesma ordem original, exceto
# por um detalhe: todas as vogais devem vir antes dos demais caracteres.

def vogais_primeiro(frase):  # recebe uma string como parâmetro
    vogais = ''
    outros = ''

    for letra in frase:
        if letra in 'aeiouAEIOU':
            vogais += letra
        else:
            outros += letra

    nova_string = vogais + outros

    return nova_string


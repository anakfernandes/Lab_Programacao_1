# Remove Caracteres

# Escreva a função remove_caracteres(frase, caracteres) que recebe uma frase e uma
# sequência de caracteres e retorna uma nova frase sem os caracteres especificados no
# segundo parâmetro
# Não é permitido usar o in para testar se o caractere está ou não na frase.

def remove_caracteres(frase, caracteres):
    nova_frase = ''
    for elemento in frase:
        fora = True  # a letra está fora dos caracteres especificados até que se prove o contrário
        for i in range(len(caracteres)):
            if caracteres[i] == elemento:  # se algum caractere da sequência especificada for igual a letra, significa que letra está dentro.
                fora = False
        if fora:  # se a letra estiver fora da sequência de caracteres especificados
            nova_frase += elemento

    return nova_frase

frase = "Apalavrados"
assert remove_caracteres(frase, "sodA") == "palavra"
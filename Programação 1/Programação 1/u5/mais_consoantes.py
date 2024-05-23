# Mais Consoantes

# Escreva um programa que leia e conte as palavras da entrada até encontrar alguma com
# número de consoantes maior que o de vogais (assuma palavras sem acentos e/ou caracteres
# especiais)

contador = 0
while True:
    palavra = input().lower()

    vogais = []
    consoantes = []
    for letra in palavra:
        if letra in "aeiou":
            vogais.append(letra)
        else:
            consoantes.append(letra)
    contador += 1
    if len(vogais) < len(consoantes):
        break

print(contador)

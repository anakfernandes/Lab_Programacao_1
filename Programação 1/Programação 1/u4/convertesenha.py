# Criptografando uma Senha

# Escreva um programa que codifica palavras usando um sistema simples de criptografia que
# consiste na substituição das letras de uma palavra por números considerando o seguinte
# mapeamento: A letra a é substituída pelo número 4. A letra e é substituída pelo número 3.
# A letra i é substituída pelo número 1. A letra o é substituída pelo número 0. Importante
# considerar que a regra de conversão não se aplica na primeira letra da palavra.

palavra = input()  # palavra a ser convertida

trocas = 0
nova_palavra = palavra[0]  # A nova palavra começa com a primeira letra de palavra
for i in range(1, len(palavra)):
    caractere = palavra[i]
    if palavra[i] == 'a' or palavra[i] == 'A':
        caractere = '4'
        trocas += 1
    if palavra[i] == 'e' or palavra[i] == 'E':
        caractere = '3'
        trocas += 1
    if palavra[i] == 'i' or palavra[i] == 'I':
        caractere = '1'
        trocas += 1
    if palavra[i] == 'o' or palavra[i] == 'O':
        caractere = '0'
        trocas += 1

    nova_palavra += caractere

print(f'{nova_palavra} ({trocas} troca(s))')

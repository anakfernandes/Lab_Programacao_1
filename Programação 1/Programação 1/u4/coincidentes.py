# Letras coincidentes

# Escreva um programa que identifica letras coincidentes em duas
# palavras. Duas palavras têm letras coincidentes se na mesma
# posição relativa a partir do início da palavra, têm a mesma
# letra. Por exemplo, as palavras 'gato' e 'sapato' têm uma única
# letra coincidente: a letra 'a' na segunda posição da palavra.

palavra1 = input()
palavra2 = input()

menor = palavra1  # Encontrando a menor palavra
if len(palavra1) > len(palavra2):
    menor = palavra2

tamanho_total = len(palavra1) + len(palavra2)

print('Letras coincidentes')

cont = 0
for i in range(len(menor)):  # iterando sob o len da menor palavra
    if palavra1[i] == palavra2[i]:  # Encontrando as letras coincidentes
        print(f"'{menor[i]}' na posição {i + 1}")
        cont += 1

porcentagem = (cont * 100) / tamanho_total
print(f'Total de letras coincidentes: {cont} ({porcentagem:.0f}%)')

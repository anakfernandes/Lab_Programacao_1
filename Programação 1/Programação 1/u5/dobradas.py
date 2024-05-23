n = int(input())


for j in range(n):
    palavra = input()

    dobrada = 0
    palavras_dobradas = []
    for i in range(len(palavra) - 1):
        if palavra[i] == palavra[i + 1]:
            palavras_dobradas.append(palavra)
            dobrada += 1
print(palavras_dobradas)

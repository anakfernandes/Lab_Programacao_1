N = int(input())

dobradas = []
nao_dobradas = []
for i in range(N):
    palavra = input()
    for j in range(len(palavra) - 1):
        if palavra[j] == palavra[j + 1]:
            dobradas.append(palavra)
            break
        elif j == len(palavra) - 2:
            nao_dobradas.append(palavra)

print(f"{len(dobradas)} palavra(s) com letras dobradas:")
for dobrada in dobradas:
    print(dobrada)
print("---")
print(f"{len(nao_dobradas)} palavra(s) sem letras dobradas:")
for nao_dobrada in nao_dobradas:
    print(nao_dobrada)
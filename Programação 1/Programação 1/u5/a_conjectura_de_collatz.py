# A conjectura de Collatz

n = int(input())

sequencia = [n]
while True:
    if n == 1:
        sequencia.append(n)
        break

    if n % 2 == 0:  # se o número for par
        n = n // 2
        sequencia.append(n)
        print(sequencia)
        continue
    if n % 2 == 1:  # se o número for ímpar
        n = (n * 3) + 1
        sequencia.append(n)

print(f"{len(sequencia)} elementos")

# Conta diferentes

def conta_diferentes(s1, s2):

    menor = len(s1)
    if len(s2) < menor:
        menor = len(s2)

    cont = 0
    for i in range(menor):
        if s1[i] != s2[i]:
            cont += 1

    return cont

assert conta_diferentes('aaa', 'bbb') == 3
assert conta_diferentes('oi', 'ola') == 1
assert conta_diferentes('ola', 'oi') == 1

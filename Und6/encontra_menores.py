def encontra_menores(num, lista):
    for elemento in lista:
        if elemento < num:
            return elemento
    return -1
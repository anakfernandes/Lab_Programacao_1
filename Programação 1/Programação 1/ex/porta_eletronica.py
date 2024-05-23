# Porta Eletrônica

def conta_categoria(categoria, lista):
    contador = 0
    for elemento in lista:
        if categoria == elemento:
            contador += 1

    return contador  # retorna a quantidade de registros de determinada categoria


categorias = []
while True:
    entrada = input()
    valores = entrada.split()

    if entrada == 'S':  # Ele encerra ao encontrar uma linha com o caractere S (de saída)
        break

    else:
        if len(entrada) == 8:  # registro
            categorias.append(valores[1][0])

        elif len(entrada) == 3:  # pesquisa
            busca = valores[1]
            print(conta_categoria(busca, categorias))

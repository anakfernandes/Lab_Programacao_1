# Binary Coded Decimal

def converte_bcd(numero):  # recebe como parâmetro uma string

    bcd_1 = ''  # separa o primeiro bcd
    for i in range(4):
        bcd_1 += numero[i]

    bcd_2 = ''  # separa o segundo bcd
    for i in range(4, 8):
        bcd_2 += numero[i]

    bcd = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001']
    decimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    decimal_1 = 0
    decimal_2 = 0
    validacao = True  # ambos os números foram convertidos até que se prove o contrário
    for i in range(10):  # converte cada bcd para decimal
        if bcd_1 == bcd[i]:
            decimal_1 = decimal[i]
        if bcd_2 == bcd[i]:
            decimal_2 = decimal[i]

    if decimal_1 == 0 or decimal_2 == 0:  # se pelo menos um número não foi convertido, BCD inválido
        validacao = False

    if validacao:
        resultado = decimal_1 + decimal_2

    else:
        resultado = 'BCD inválido.'

    return resultado


while True:
    entrada = input()

    if entrada == 'fim':
        break

    elif len(entrada) != 8:
        print('Tente novamente.')
        continue

    else:
        print(converte_bcd(entrada))


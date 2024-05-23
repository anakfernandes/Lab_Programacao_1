def calcula_digito(cpf):
    multiplo = 2
    soma = 0
    for i in range(len(cpf) - 1, -1, -1):
        multiplicacao = int(cpf[i]) * multiplo
        soma += multiplicacao
        multiplo += 1
    digito1 = str((10 * soma) % 11)
    if digito1 == '10':
        digito1 = '0'
    return digito1

def calcula_digitos_verificacao(cpf):
    digito1 = calcula_digito(cpf)
    digito2 = calcula_digito(cpf + digito1)
    return digito1 + digito2

assert calcula_digitos_verificacao('153245875') == '40'
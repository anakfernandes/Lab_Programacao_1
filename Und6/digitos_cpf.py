def calcula_digito(num_cpf):
    multiplicador = 2
    multiplica_dig = 0
    for i in range(len(num_cpf) - 1, - 1, -1):
        multiplica_dig += int(num_cpf[i]) * multiplicador
        multiplicador += 1
    digito = (10 * multiplica_dig) % 11
    if digito == 10:
        digito = 0
    return str(digito)


def calcula_digitos_verificacao(num_cpf):
    digito1 = calcula_digito(num_cpf)
    digito2 = calcula_digito(num_cpf + digito1)
    return digito1 + digito2
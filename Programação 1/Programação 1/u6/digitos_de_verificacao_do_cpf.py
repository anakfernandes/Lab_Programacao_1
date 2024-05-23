def calcula_digitos_verificacao(cpf):  # recebemos uma string de 9 dígitos como parâmetro
    # convertendo de str para int
    cpf_int = []
    for i in range(len(cpf)):
        cpf_int.append(int(cpf[i]))
    # calculando o primeiro dígito de verificação
    soma = 0
    cont = 0
    for elemento in cpf_int:
        soma += elemento * (10 - cont)
        cont += 1
# Se uma das expressões dos dígitos verificadores resultar em 10, o dígito efetivo será 0 (zero).
    if (soma * 10) % 11 == 10:
        primeiro_digito = 0
    else:
        primeiro_digito = (soma * 10) % 11

    # calculando o segundo dígito de verificação
    cpf += str(primeiro_digito)

    cpf_int = []
    for i in range(len(cpf)):  # convertendo de str para int
        cpf_int.append(int(cpf[i]))

    soma = 0
    cont = 0
    for elemento in cpf_int:
        soma += elemento * (11 - cont)
        cont += 1

    if (soma * 10) % 11 == 10:
        segundo_digito = 0
    else:
        segundo_digito = (soma * 10) % 11

    dois_digitos = str(primeiro_digito) + str(segundo_digito)

    return dois_digitos



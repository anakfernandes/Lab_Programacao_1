# Expressão regular simples

#

def is_substring_expr(str1, str2):
# Poderia ter usado apenas um split('*')
    comeco_outrastring = 0
    umastring = ''  # Primeira string de str2
    for i in range(len(str2)):
        if str2[i] == '*':
            comeco_outrastring = i + 1  # índice do início da segunda string de str2
            break
        umastring += str2[i]

    outrastring = ''  # Segunda string de str2
    for i in range(comeco_outrastring, len(str2)):
        outrastring += str2[i]

    inicio_str1 = ''
    for i in range(len(umastring)):
        inicio_str1 += str1[i]
# Deve conter qualquer sequência não vazia,portanto str1 nao deve ser menor que str2
    if len(str1) < len(str2):
        resultado = False
    else:
        fim_str1 = ''
        for i in range(len(str1)-len(outrastring), len(str1)):
            fim_str1 += str1[i]
# O começo da str precisa ser igual a umastring. O fim de str deve ser igual a outrastring
        if umastring == inicio_str1 and outrastring == fim_str1:
            resultado = True
        else:
            resultado = False

    return resultado




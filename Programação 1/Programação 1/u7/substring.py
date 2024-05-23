# Verificando se uma String é Substring de Outra String

#Escreva uma função is_substring(str1, str2) que verifica se str2 está em str1. Em caso
# afirmativo, a função deve retornar True. Caso contrário, deve retornar False.

def is_substring(str1, str2):
    if len(str2) > len(str1):  # Retorne Falso se str2 for maior que str1
        return False
    for i in range(len(str1)):
        iguais = 0
        for j in range(len(str2)):
            if str2[j] != str1[j + i]:
                break
            else:
                iguais += 1
                if iguais == len(str2):  # Se o número de letras iguais for igual ao tamanho da substring analisada
                    return True
    return False


assert is_substring('tudobomcon', 'bom')
assert is_substring('boiada', 'oi')
assert not is_substring('casoriocasa', 'casajsdjfjdsgjdsgj')
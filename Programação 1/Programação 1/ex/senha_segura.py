# Senha Segura

# Uma senha segura é composta por um número de pelo menos 4 dígitos, cujos algarismos nas
# posições ímpares são todos ímpares e que os algarismos nas posições pares são todos pares
# . Por exemplo: Considere a senha segura 7852. O primeiro algarismo (7) e o terceiro
# algarismo (5) são ímpares. O segundo algarismo (8) e o quarto algarismo (2) são pares.
# Crie uma função que recebe uma senha numérica e verifica se essa senha é segura ou
# insegura.

def senha_segura(senha):

    resultado = True  # A senha é segura até que se prove o contrário

    if len(senha) < 4:
        resultado = False
    else:
        for i in range(0, len(senha), 2):  # posições ímpares
            if int(senha[i]) % 2 != 1:  # Se algum número não for ímpar
                resultado = False

        for i in range(1, len(senha), 2):  # posições pares
            if int(senha[i]) % 2 != 0:  # Se algum número não for par
                resultado = False

    if resultado:
        return "Senha segura"

    return "Senha insegura"


assert senha_segura("12346") == "Senha insegura"
assert senha_segura("125638") == "Senha segura"
assert senha_segura("1") == "Senha insegura"
assert senha_segura("1256") == "Senha segura"
assert senha_segura("1246") == "Senha insegura"
assert senha_segura("2256") == "Senha insegura"
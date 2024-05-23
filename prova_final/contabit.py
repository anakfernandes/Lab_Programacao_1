# UFCG
# ana.fernandes@ccc.ufcg.edu.br Turma: 21.2
# Solução Conta Bits Um

def contar(lista):
    cont = 0
    for i in range(len(lista)):
        cont += 1
    return str(cont)

while True:
    bits = input()
    if bits == '0101010101': break
    bits = bits.split('0')
    retorno = ''
    for i in range(len(bits)):
 
        if bits[i] != '':
            if retorno == '':
                retorno +=  contar(bits[i])
            else:
                retorno += ' '
                retorno +=  contar(bits[i])
    print(retorno)
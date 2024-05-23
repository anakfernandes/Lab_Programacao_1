# Split Simplificado

# Implemente a função split_simplificado(frase) que tokeniza (divide em tokens ou pedaços)
# uma dada string considerando o espaço em branco como delimitador. A função deve retornar
# uma lista contendo todos os tokens separados. Ou seja, a função implementada split_simpli
# ficado(frase) tem efeito semelhante ao produzido por Python quando executar frase.split()

def split_simplificado(frase): # 'oi som te  '

    lista_tokens = []
    token = ''
    for i in range(len(frase)):
        if frase[i] != ' ':
            token += frase[i]
            if len(frase) - 1 == i:
                lista_tokens.append(token)
        else:
            if token != '':
                lista_tokens.append(token)
                token = ''

    return lista_tokens

print(split_simplificado('oi   tudo r     bem'))
print('oi   tudo r     bem'.split())

assert split_simplificado('um exemplo') == ['um','exemplo']
assert split_simplificado('um exemplo') == 'um exemplo'.split()
assert split_simplificado('testando') == 'testando'.split()


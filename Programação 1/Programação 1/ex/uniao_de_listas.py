# União de Listas

# Implemente a função uniao_listas(l1,l2) que calcula a união entre as duas listas passadas
# como parâmetro. Sua função deve alterar a l1 para conter todos os elementos das duas lis-
# tas (sem repetição).

def uniao_listas(l1, l2):

    for elemento in l2:
        achou = False
        for valor in l1:
            if elemento == valor:
                achou = True
        if not achou:
            l1.append(elemento)


l1 = [2,1,3,4]
l2 = [2]
assert uniao_listas(l1,l2) == None
assert l1 == [2,1,3,4]
assert l2 == [2]

l1 = [1,3,4]
l2 = [4]
assert uniao_listas(l1,l2) == None
assert l1 == [1,3,4]
assert l2 == [4]

l1 = [2,4,1]
l2 = [6,7,91]
uniao_listas(l1,l2)
assert l1 == [2,4,1,6,7,91]
assert l2 == [6,7,91]

l1 = [2,4,1]
l2 = [7,7,7]
uniao_listas(l1,l2)
assert l1 == [2,4,1,7]
assert l2 == [7,7,7]

l1 = [2,4,1]
l2 = [2,4,1]
uniao_listas(l1,l2)
assert l1 == [2,4,1]
assert l2 == [2,4,1]
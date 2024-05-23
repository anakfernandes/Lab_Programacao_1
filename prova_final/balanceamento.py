# UFCG
# ana.fernandes@ccc.ufcg.edu.br Turma: 21.2
# Solução Balanceamento entre Raposeiros e Trezeanos 

lista_c = []
lista_t = []
cont_i = 1

while True:
    time = input()
    if time == 'c':
        lista_c.append(cont_i)
    else:
        lista_t.append(cont_i) 
    if len(lista_c) > len(lista_t):  
        if (len(lista_c) - len(lista_t)) > 2:
            break
    else:
        if (len(lista_t) - len(lista_c)) > 2:
            break
    cont_i += 1
if len(lista_c) > len(lista_t):
    print('RAPOSEIROS em maior quantidade')
else:
    print('TREZEANOS em maior quantidade')

print('TREZEANOS:')
for i in range(len(lista_t)):
    print(lista_t[i])
print('RAPOSEIROS:')
for j in range(len(lista_c)):
    print(lista_c[j])
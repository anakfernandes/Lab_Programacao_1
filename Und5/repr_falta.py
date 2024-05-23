# UFCG
# Programação 1  Turma: 2022.1
# ana.fernandes@ccc.ufcg.edu.br
# Solução Reprovados por falta

reprovados = 0
quantidade_falta = 0

while True:
    registro = input()    
    if registro != '-':
        quantidade_falta = 0
        cont = 0
        while cont < len(registro):
            if registro[cont] == 'f':
                quantidade_falta += 1
            cont += 1
        if quantidade_falta > 8:
            reprovados += 1
    else:
        break
print(f'{reprovados} aluno(s) reprovado(s) por falta.')

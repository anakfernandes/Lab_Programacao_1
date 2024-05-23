alunos_reprovados = 0
while True:
    frequencia = input()
    iterador = iter(frequencia)
    faltas = 0
    while True:
        try:
            objeto = next(iterador)
            if objeto == "f":
                faltas += 1
        except StopIteration:
            break
    if faltas > 8:
        alunos_reprovados += 1
    if frequencia == "-":
        break
print(f"{alunos_reprovados} aluno(s) reprovado(s) por falta.")

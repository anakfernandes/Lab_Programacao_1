# UFCG
# Programação 1  Turma: 22.1
# ana.fernandes@ccc.ufcg.edu.br
# Solução para <https://p1ufcg.github.io/#/as/5428000008962048>

cpf1 = int(input())
cpf2 = int(input())
cpf3 = int(input())

format_cpf1 = cpf1 // 100
resto1 = cpf1 % 100
soma1 = (resto1 // 10) + (resto1 % 10)

format_cpf2 = cpf2 // 100
resto2 = cpf2 % 100
soma2 = (resto2 // 10) + (resto2 % 10)

format_cpf3 = cpf3 // 100
resto3 = cpf3 % 100
soma3 = (resto3 // 10) + (resto3 % 10)

print(f'{format_cpf1}-{resto1}')
print(soma1)

print(f'{format_cpf2}-{resto2}')
print(soma2)

print(f'{format_cpf3}-{resto3}')
print(soma3)
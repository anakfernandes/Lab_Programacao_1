# UFCG
# Programação 1  Turma: 22.1
# ana.fernandes@ccc.ufcg.edu.br
# Solução para <https://p1ufcg.github.io/#/as/6588151072030720>

capacidade_revs = float(input('Capacidade de revestimento? '))
print(f'\n== Dados do vão a revestir ==')

comprimento = float(input('Comprimento? '))
largura = float(input('Largura? '))
altura = float(input('Altura? '))

area = (2 * comprimento * largura) + (2 * comprimento * altura) + (2 * largura * altura)
teto = comprimento * largura
area_total = area - teto
num_caixas = int(area_total / capacidade_revs)

print(f'\n== Resultados ==')
print(f'Área total a revestir: {area_total} m2')
print(f'Número de caixas: {num_caixas}')
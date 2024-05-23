# Mínimo, média e máximo

#  O pesquisador, contudo, precisa adicionar a cada linha de dados os valores mínimo,
#  médio e máximo observados até aquela medição.

n = int(input())  # Número de dados contidos na sequência de dados

dados = []
soma = 0
cont = 1
while cont < n + 1:
    dado = float(input())  # leitura dos dados no formato bruto
    dados.append(dado)
    soma += dado

    maximo = dados[0]  # valor máximo até o momento
    for i in range(len(dados)):
        if dados[i] > maximo:
            maximo = dados[i]

    minimo = dados[0]  # valor mínimo até o momento
    for i in range(len(dados)):
        if dados[i] < minimo:
            minimo = dados[i]

    media = soma / cont
    print(f'{dado:.0f} {minimo:.0f} {media:.2f} {maximo:.0f}')  # valores observados até aquela medição
    cont += 1

# Maioridade Penal Função

# Escreva uma função chamada maioridade_penal que informe o nome das pessoas que atingiram
# a maioridade penal (idade >= 18). O programa recebe duas strings. A primeira com nomes de
# pessoas e a segunda com as idades destas pessoas (separadas por espaço). O programa
# retorna uma string com os nomes das pessoas que atingiram a maioridade penal, na mesma
# ordem em que foram recebidos na entrada. Assuma que a quantidade de pessoas e de idades
# será sempre igual. Caso não haja pessoas 'maiores de idade' o programa deve retornar uma
# string vazia.

def maioridade_penal(nomes, idades):  # recebe dois parâmetros do tipo string
    lista_nomes = nomes.split()
    lista_idades = idades.split()

    maiores = ''  # filtrando as pessoas maiores de idade
    for i in range(len(lista_idades)):
        if int(lista_idades[i]) >= 18:   # convertendo de str para int e comparando
            maiores += lista_nomes[i] + ' '

    return maiores.strip()

print(maioridade_penal('',''))
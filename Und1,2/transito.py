dia1 = int(input())
dia2 = int(input())
dia3 = int(input())
dia4 = int(input())
dia5 = int(input())

soma = dia1 + dia2 + dia3 + dia4 + dia5
media = soma / 5
ptempo = soma * 100 / 7200

numep = soma // 50

print(f'Você perdeu {soma} min na semana (média de {media:.1f} min por dia).')
print(f'Isso significa {ptempo:.2f}% da sua semana produtiva.')
print(f'Daria para assistir {numep} episódio(s) de House.')
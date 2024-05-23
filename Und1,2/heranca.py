hectares = int(input())
herdeiros = int(input())
heranca = hectares // herdeiros
doacao = hectares % herdeiros
print(f'Cada herdeiro deverá receber {heranca} hectare(s).')
print(f'{doacao} hectare(s) para doação.') 
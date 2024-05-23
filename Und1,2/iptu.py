area = float(input('Área construída? '))
aliquota = float(input('Alíquota? '))

iptu  = (area * aliquota) + 35.00
print(f'IPTU: R$ {iptu:.2f}')

cotaunica = (iptu - ((iptu * 25) / 100))

seisp = (iptu - ((iptu * 5) / 100)) 
fseis = seisp / 6

dezp = iptu
fdez = dezp / 10


print('\nPagamento:')
print(f'1. Quota única. R$ {cotaunica:.2f}')
print(f'2. Em 6 parcelas. Total: R$ {seisp:.2f}')
print(f'   6 x R$ {fseis:.2f}')
print(f'3. Em 10 parcelas. Total: R$ {dezp:.2f}')
print(f'   10 x R$ {fdez:.2f}')

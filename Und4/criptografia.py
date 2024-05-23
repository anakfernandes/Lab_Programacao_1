senha = input()
acumulador = 0
nova_senha = ""

for x in range(len(senha)):
    if x != 0:
        if senha[x] == 'a' or senha[x] == 'A':
            nova_senha += '4'
            acumulador += 1
        elif senha[x] == 'e' or senha[x] == 'E':
             nova_senha += '3'
             acumulador += 1
        elif senha[x] == 'i' or senha[x] == 'I':
             nova_senha += '1'
             acumulador += 1
        elif senha[x] == 'o' or senha[x] == 'O':
             nova_senha += '0'
             acumulador += 1
        else:
             nova_senha += senha[x]
    else:
        nova_senha += senha[x]
        
print(f'{nova_senha} ({acumulador} troca(s))')

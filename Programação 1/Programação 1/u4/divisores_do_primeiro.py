# Soma os Divisores do Primeiro Elemento de uma Lista

# Escreva um programa que leia 11 números inteiros. O primeiro valor lido é o valor de
# referencia. O programa deve imprimir a soma dos números lidos que são divisores do
# número de referência. Atenção, o primeiro (número de referência) dos 11 números não
# deve entrar na soma.


referencia = int(input())  # valor de referência
soma_divisores = 0
for i in range(10):
    n = int(input())
    if referencia % n == 0:
        soma_divisores += n  # Soma apenas os números que são divisores do valor de referência
print(soma_divisores)

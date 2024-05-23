def acha_ponto_flutuante(string):
    for c in string:
        if c == '.':
            return True
    return False



def ordena_tipos(array):
    for j in range(len(array)):
        for i in range(len(array) - 1):
            if array[i].isalpha():  # se for letra
                if array[i + 1].isdigit() and not acha_ponto_flutuante(array[i + 1]):  # se o vizinho for inteiro
                    array[i], array[i + 1] = array[i + 1], array[i]

            if array[i].isalnum() and not array[i].isalpha() and not array[i].isnumeric() or acha_ponto_flutuante(array[i]):
                if array[i + 1].isdigit() and not acha_ponto_flutuante(array[i + 1]) or array[i + 1].isalpha():
                    array[i], array[i + 1] = array[i + 1], array[i]

a = ['1a', '2', 'e', '4', '4.4', 'e6', '8']
ordena_tipos(a)
print(a)
assert ordena_tipos(a) == None
assert a == ['2', '4', '8', 'e', '1a', '4.4', 'e6']


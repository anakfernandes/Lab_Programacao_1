antes = float(input())
depois = float(input())

porcentagem = (antes - depois) / antes * 100

if porcentagem <= 5:
    print(f'{porcentagem:.1f}% do peso do produto é de água congelada.')
    print('Produto qualis A.')

elif porcentagem > 5 and porcentagem <= 10:
    print(f'{porcentagem:.1f}% do peso do produto é de água congelada.')
    print('Produto em conformidade.')

else:
    print(f'{porcentagem:.1f}% do peso do produto é de água congelada.')
    print('Produto não conforme.')
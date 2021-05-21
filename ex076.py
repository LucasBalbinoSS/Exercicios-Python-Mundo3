listagem = ('Lápis', 1.75,
            'Borracha', 2.50,
            'Tesoura', 3.50,
            'Caderno', 25.30,
            'Lapiseira', 7.37,
            'Mochila', 50.10,
            'Garrafinha', 15.70,
            'Lápis de cor', 15.80,
            'Canetas', 10.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>6.2f}')
print('-' * 40)

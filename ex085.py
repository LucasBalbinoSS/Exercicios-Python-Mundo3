lista_nums = list()
lista_nums_par = list()
lista_nums_impar = list()

lista_nums.append(lista_nums_impar)
lista_nums.append(lista_nums_par)

for cont in range(0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        lista_nums_par.append(num)
    else:
        lista_nums_impar.append(num)

print()
if len(lista_nums_par) == 0:
    print('Você não digitou nenhum número par...')
else:
    print(f'Você digitou {len(lista_nums_par)} números pares.')
    print('Sua lista completa de números pares em ordem crescente: ', end=' ')
    for n in sorted(lista_nums_par):
        print(f'{n}... ', end='')

print()
if len(lista_nums_impar) == 0:
    print('\nVocê não digitou nenhum número ímpar...')
else:
    print(f'Você digitou {len(lista_nums_impar)} números ímpares.')
    print('Sua lista de números ímpares em ordem crescente: ', end=' ')
    for n2 in sorted(lista_nums_impar):
        print(f'{n2}... ', end='')

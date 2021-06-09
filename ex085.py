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

print('Sua lista completa de números pares em ordem crescente: ', end=' ')
for n in sorted(lista_nums_par):
    print(f'{n}... ', end='')

print('\nSua lista de números ímpares em ordem crescente: ', end=' ')
for n2 in sorted(lista_nums_impar):
    print(f'{n2}... ', end='')

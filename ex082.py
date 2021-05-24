lista_num = list()
lista_num_par = list()
lista_num_impar = list()

while True:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        lista_num_par.append(num)

    elif num % 2 == 1:
        lista_num_impar.append(num)
    lista_num.append(num)

    continuar = str(input('Quer continuar? [ S / N ] ')).strip().upper()
    print()
    if continuar[0] == 'N':
        break

    while continuar[0] != 'S' and continuar[0] != 'N':
        continuar = str(input('Quer continuar? [ S / N ] ')).strip().upper()
        print()

print('=-' * 30)

print(f'Lista completa: ', end='')
print(f'{lista_num}')

print()

print('Lista de números pares: ', end='')
if len(lista_num_par) == 0:
    print('\não houveram números pares...')
else:
    print(f'{lista_num_par}')

print()

print('Lista de números ímpares: ', end='')
if len(lista_num_impar) == 0:
    print('não houveram números ímpares...')
else:
    print(f'{lista_num_impar}')

print('=-' * 30)

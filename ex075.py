numeros = (int(input('\033[1mDigite um número: ')),
           int(input('Digite outro valor: ')),
           int(input('Digite mais um número: ')),
           int(input('Só mais um: ')))
print()

print(f'\033[mVocê digitou os números {numeros}')

if 9 not in numeros:
    print('O número 9 não foi digitado nenhuma vez')
else:
    print(f'O número 9 foi digitado \033[1;4m{numeros.count(9)} vezes\033[m')

if 3 not in numeros:
    print('O número 3 não foi está em nenhuma posição')
else:
    print(f'O número 3 aparece na posição de número \033[1;4m{numeros.index(3) + 1}\033[m')

print('Os valores pares digitados foram:', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
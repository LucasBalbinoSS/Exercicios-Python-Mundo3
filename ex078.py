numeros = list()
maior = 0
menor = 0

for cont in range(0, 5):
    numeros.append(int(input(f'Digite o {cont}° valor: ')))

    if cont == 0:
        maior = menor = numeros[cont]

    elif numeros[cont] > maior:
        maior = numeros[cont]

    elif numeros[cont] < menor:
        menor = numeros[cont]

print()
print(f'O \033[1;4mmaior\033[m valor digitado foi {max(numeros)}', end='')
print(f' que está nas posições ', end='')

for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}... ', end='')

print(f'\nO \033[1;4mmenor\033[m valor digitado foi {menor}', end=' ')

for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}... ', end='')
print(f'\n e se encontra na {numeros.index(min(numeros)) + 1}° posição')
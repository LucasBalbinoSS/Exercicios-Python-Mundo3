numeros = list()

for cont in range(1, 6):
    numeros.append(int(input(f'Digite o {cont}° valor: ')))

print()
print(f'O \033[1;4mmaior\033[m valor digitado foi {max(numeros)}', end='')
print(f' que está na {numeros.index(max(numeros)) + 1}° posição')
print(f'O \033[1;4mmenor\033[m valor digitado foi {min(numeros)}', end='')
print(f' e se encontra na {numeros.index(min(numeros)) + 1}° posição')
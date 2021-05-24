numeros = list()

while True:
    num = int(input('Digite um número: '))

    if num in numeros:
        print('\033[33mEsse valor já existe na lista, não vou adicionar...\033[m')
        print()

    else:
        numeros.append(num)
        print('\033[1;36mValor adicionado com sucesso!\033[m')
        print()

    continuar = str(input('Você deseja continuar? [ S / N ] ')).upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('ERRO! você deseja continuar? [ S / N ] ')).upper().strip()

    if continuar == 'N':
        break

print('-=' * 30)
print()
print(f'Você digitou os valores {sorted(numeros)}')

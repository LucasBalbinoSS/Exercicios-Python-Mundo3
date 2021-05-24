from time import sleep as slp

listaNum = list()
contadorde5 = 0

while True:
    num = int(input('Digite um número: '))
    if num == 5:
        contadorde5 += 1
    listaNum.append(num)

    continuar = str(input('Quer continuar? [ S / N ] ')).strip().upper()
    print()

    if continuar[0] == 'N':
        break

    while continuar[0] != 'S' and continuar[0] != 'N':
        continuar = str(input('Quer continuar? [ S / N ] ')).strip().upper()
        print()

print('=-' * 35)
print(f'Sua lista ficou assim: {listaNum}')
print('=-' * 35)
print(f'Foram digitados {len(listaNum)} números!')
print(f'A lista de forma descrescente se torna {sorted(listaNum, reverse=True)}')
print('=-' * 35)

if 5 in listaNum:
    print(f'O valor 5 está sim na lista!\nEncontrei {contadorde5} deles!')
else:
    print('Não encontrei nenhum número 5 na lista...')
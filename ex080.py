lista = list()

for cont in range(0, 5):
    num = int(input('Digite um número: '))
    if cont == 0 or num > lista[-1]:
        lista.append(num)
        print('\033[35;1mValor adicionado ao final da lista!\033[m')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'valor adicionado na posição {pos} da lista...')
                break
            pos += 1

print('-=' * 30)
print(lista)
lista = list()

for cont in range(0, 5):
    num = int(input('Digite um número: '))
    if len(lista) == 0:
        lista.append(num)
        print('\033[35;1mPrimeiro valor dicionado à lista!\033[m')

    elif len(lista) == 1 and num >= lista[0]:
        lista.append(num)
        print('\033[35;1mValor adicionado na segunda posição!\033[m')
    else:
        lista.insert(0, num)
        print('\033[35;1mValor adicionado na primeira posição da lista!\033[m')
        print(lista)

print(lista)
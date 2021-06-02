lista = list()

for cont in range(0, 5):
    num = int(input('Digite um número: '))
    if len(lista) == 0:
        lista.append(num)
        print('\033[35;1mPrimeiro valor dicionado à lista!\033[m')

print(lista)
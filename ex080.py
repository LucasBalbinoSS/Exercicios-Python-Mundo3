lista = list()

for cont in range(0, 5):
    num = int(input('Digite um número: '))
    if len(lista) <= 2:
        lista.append(num)
        print('Adicionado na lista!')
    elif len(lista) > 2:
        pass

print(lista)
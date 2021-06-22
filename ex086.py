lista = [0] * 3

for i in range(len(lista)):
    lista[i] = [0] * 3

    for j in range(len(lista[i])):
        lista[i][j] = int(input('Digite um número: '))

print()
for i in range(len(lista)):
    for j in range(len(lista[i])):
        print(lista[i][j], end='\t')
    print('')
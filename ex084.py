listaDados = list()
pessoas = list()

while True:
    pessoas.append(str(input('Digite seu nome: ')).strip().title())
    pessoas.append(int(input('Digite seu peso (em Kg): ')))
    print()

    listaDados.append(pessoas[:])
    pessoas.clear()

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        print()
    if resp == 'N':
        break

for p in range(len(listaDados)):
    print(listaDados[p][1])
    if listaDados[p][1] > listaDados[p][1]:
        print(f'O maior valor encontrado foi {listaDados[p][1]}')

print('=-' * 30)
print(' ' * 15, '\033[34;1;4mANÁLISE DE DADOS\033[m')
print()

print(listaDados)
if len(listaDados) == 1:
    print(f'{len(listaDados)} pessoa foi cadastrada.')
else:
    print(f'{len(listaDados)} pessoas foram cadastradas.')

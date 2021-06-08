listaDados = list()
pessoas = list()
nomes_mais_pesadas = list()
maior_peso = list()

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
    if len(listaDados) == 1:
        maior_peso.append(listaDados[p][1])
        # nomes_mais_pesadas.append(listaDados[p][0])

    elif len(listaDados) > 1 and listaDados[p][1] > maior_peso[0:]:
        maior_peso.append(listaDados[p][1])
        nomes_mais_pesadas.append(listaDados[p][0])

print(maior_peso)
print(nomes_mais_pesadas)

print('=-' * 30)
print(' ' * 15, '\033[34;1;4mANÁLISE DE DADOS\033[m')
print()

print(listaDados)
if len(listaDados) == 1:
    print('Apenas uma pessoa foi cadastrada.')
else:
    print(f'No total, {len(listaDados)} pessoas foram cadastradas.')

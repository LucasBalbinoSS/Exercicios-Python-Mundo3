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
    if resp == 'N':
        break
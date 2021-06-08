listaDados = list()
pessoas = list()

for p in range(0, 5):
    pessoas.append(str(input('Digite seu nome: ')).strip().title())
    pessoas.append(int(input('Digite seu peso: Kg')))

    listaDados.append(pessoas[:])
    pessoas.clear()
database = list()
nome = list()
peso = list()
cont = 0

while True:
    nome.append(str(input('Digite seu nome: ')).strip().title())
    peso.append(int(input('Digite seu peso: ')))
    database.append(nome[:])
    database.append(peso[:])

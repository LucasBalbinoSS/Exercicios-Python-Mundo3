campeonato = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo',
              'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR',
              'Bragantino', 'Ceará SC', 'Corinthans', 'Atlético-GO', 'Bahia',
              'Sport Recife', 'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba',
              'Botafogo')

print('\033[1;4mPRIMEIROS CINCO COLOCADOS\033[m:')
print(campeonato[0:5])
print()

print('\033[1;4mÚLTIMOS QUATRO COLOCADOS\033[m:')
print(campeonato[16:21])
print()

print('\033[1;4mOS COLOCADOS EM ORDEM ALFABÉTICA\033[m:')
print(sorted(campeonato))
print()

print('\033[1;4mEM QUAL ÍNDICE SE ENCONTRA O BOTAFOGO?\033[m:')
print('O time do Botafogo se encontra na {}° posição'.format(campeonato.index('Botafogo') + 1))

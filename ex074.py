from random import randint as rdt

contador = 0
numeros = (rdt(0, 10), rdt(0, 10), rdt(0, 10), rdt(0, 10), rdt(0, 10))

print(f'Os números sorteados foram: {numeros}')
print(f'O maior número sorteado foi o número {max(numeros)}')
print(f'O menor número sorteado foi o número {min(numeros)}')

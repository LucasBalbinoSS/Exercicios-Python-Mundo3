numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

while True:
    numusuario = int(input('Digite um número: '))

    while numusuario > 20 or numusuario < 0:
        numusuario = int(input('Erro! digite um número entre 0 e 20: '))
    print('Você digitou o número \033[1;4;35m%s\033[m' % numeros[numusuario])

    continuar = str(input('Você deseja continuar? [ S / N ]: ')).strip().upper()
    print()

    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Você deseja continuar? [ S / N ]: ')).strip().upper()
        print()

    if continuar == 'S':
        continue

    elif continuar == 'N':
        break
print('Tenha um bom dia!')
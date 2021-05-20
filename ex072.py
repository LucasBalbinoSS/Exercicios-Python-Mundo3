numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numusuario = int(input('Digite um número: '))
while numusuario > 20 or numusuario < 0:
    numusuario = int(input('Erro! digite um número entre 0 e 20: '))
print('Você digitou o número \033[1;4;35m%s' % numeros[numusuario])

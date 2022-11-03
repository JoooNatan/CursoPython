from random import randint#gera um numero int aleatorio
tentativas = 1

rand = randint(0, 10)#gera um numero aleatorio entre 0 e 10
num = int(input('Tente advinhar o numero (de 0 a 10) '))

if rand == num:
    print('\033[32mParabens voce acertou com uma unica tentativa!\033[m')
else:
    while rand != num:
        if rand > num:
            num = int(input('\033[31mVoce errou\033[m, tente um numero maior: '))
        else:
            num = int(input('\033[31mVoce errou\033[m, tente um numero menor: '))
        tentativas += 1
        print('-' * 40)
    print('Voce acertou em {} tentativas'.format(tentativas))

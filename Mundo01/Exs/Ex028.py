'''import random
p = int(input('Tente advinhar o numero (de 0 a 5) '))
ln = [0, 1, 2, 3, 4, 5]
e = random.choice(ln)
print('O numero sorteado foi {}'.format(e))
if p == e:
    print('Parabens voce acertou!')
else:
    print('Voce errou!')    meu jeito'''


#jeito guanabara
from random import randint#gera um numero int aleatorio
rand = randint(0, 5)#gera um numero aleatorio entre 0 e 5
num = int(input('Tente advinhar o numero (de 0 a 5) '))
print('O numero sorteado foi {}'.format(rand))

if rand == num:
    print('\033[32mParabens voce acertou!\033[m')
else:
    print('\033[31mVoce errou!\033[m')
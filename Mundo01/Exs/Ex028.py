import random
p = int(input('Tente advinhar o numero (de 0 a 5) '))
ln = [0, 1, 2, 3, 4, 5]
e = random.choice(ln)
print('O numero sorteado foi {}'.format(e))
if p == e:
    print('Parabens voce acertou!')
else:
    print('Voce errou!')
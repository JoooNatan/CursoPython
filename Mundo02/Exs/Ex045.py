from random import randint

itens = ('', 'Pedra', 'Papel', 'Tesoura')
pc = randint(1, 3)

print('-' * 20)
print('Pedra papel tesoura')
print('-' * 20)
print('''[1] Pedra
[2] Papel
[3] Tesoura''')

op = int(input('Qual sua jogada? '))
print('-' * 20)

if op > 3:
    print('Opção invalida!')
else:
    print('Pc jogou {}'.format(itens[pc]))
    print('Resultado: ', end = '')
    if pc == 1:
        if op == 1:
            print('\033[1;33mEmpate\033[m')
        elif op == 2:
            print('\033[1;32mVoce ganhou\033[m')
        else:
            print('\033[1;31mVoce perdeu\033[m')
    elif pc == 2:
        if op == 1:
            print('\033[1;31mVoce perdeu\033[m')
        elif op == 2:
            print('\033[1;33mEmpate\033[m')
        else:
            print('\033[1;32mVoce ganhou\033[m')
    else:
        if op == 1:
            print('\033[1;32mVoce ganhou\033[m')
        elif op == 2:
            print('\033[1;31mVoce perdeu\033[m')
        else:
            print('\033[1;33mEmpate\033[m')

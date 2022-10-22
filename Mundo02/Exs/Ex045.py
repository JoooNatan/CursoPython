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
    if pc == 1:
        if op == 1:
            print('Empate')
        elif op == 2:
            print('Voce ganhou')
        elif op == 3:
            print('Voce perdeu')
    elif pc == 2:
        if op == 1:
            print('Voce perdeu')
        elif op == 2:
            print('Empate')
        elif op == 3:
            print('Voce ganhou')
    else:
        if op == 1:
            print('Voce ganhou')
        elif op == 2:
            print('Voce perdeu')
        elif op == 3:
            print('Empate')

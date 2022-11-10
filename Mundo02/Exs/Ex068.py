from random import randint
v = 0

while True:
    jogador = int(input('Diga um valor: '))
    pc = randint(0, 10)
    total = jogador + pc
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {pc}. total de: {total} ', end = '')
    print('Deu par' if total % 2 == 0 else 'Deu Impar')

    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu!')
            break
        
    print('Vamos jogar novamente..')
print(f'Game Over! voce venceu {v} vezes.')

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
op = 0

while op != 5:
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    op = int(input('Opção: '))

    if op == 1:
        print('{} + {} = {}'.format(n1, n2, (n1 + n2)))

    elif op == 2:
        print('{} x {} = {}'.format(n1, n2, (n1 * n2)))

    elif op == 3:
        print('Maior numero: ', end = '')
        if n1 > n2:
            print(n1)
        else:
            print(n2)
            
    elif op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif op == 5:
        print('Fim')

    else:
        print('\033[31mOpção invalida\033[m! digite novamente')
    print('-' * 30)

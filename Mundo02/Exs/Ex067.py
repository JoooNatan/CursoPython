while True:
    n = int(input('Quer ver a tabuada de qual numero? '))
    print('-' * 38)
    if n < 0:
        print('Programa encerrado!')
        break
    else:
        for c in range (1, 11):
            print(f'{n} x {c} = {n * c}')
    print('-' * 38)

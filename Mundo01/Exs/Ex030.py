n = int(input('Digite um numero '))
if n % 2 == 0:
    print('O numero {} é \033[32mpar\033[m'.format(n))
else:
    print('O numero {} é \033[31mimpar\033[m'.format(n))
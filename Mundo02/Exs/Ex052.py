num = int(input('Digite um numero intero: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m{}\033[m'.format(c), end = ' ')
        tot += 1
    else:
        print('\033[31m{}\033[m'.format(c), end = ' ')

print('\nO numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('Por isso ele é primo.')
else:
    print('Por isso ele não é primo.')
    
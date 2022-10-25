for c in range(1, 21, 3):#1 inicio | 21 range == intervalo | terceiro numero == passo
    if c % 2 == 0:
        print('[{}]'.format(c), end=' ')
    else:
        print(c, end=' ')
print('Fim')

s = 0
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c, end = ' ')
    s = s + c

print('Soma dos valores: {}'.format(s))
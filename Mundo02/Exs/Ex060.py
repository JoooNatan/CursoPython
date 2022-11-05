num = int(input('Digite um numero: '))
c = num
f = 1

while c > 0:
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f = f * c
    c -= 1
print(f)

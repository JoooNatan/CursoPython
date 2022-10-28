p = int(input('Digite o primeiro termo '))
r = int(input('Digite a razão '))
d = p + (10 - 1) * r

for c in range(p, d + r, r):
    print('{} -> '.format(c), end = '')
print('Acabou!')
s = 0
cont = 0

for c in range(1, 500, 2):
    if c % 3 == 0:
        s = s + c
        cont = cont + 1

print('Soma dos {} valores impares que são divisiveis por 3(de 1 a ate 500): {}'.format(cont, s))

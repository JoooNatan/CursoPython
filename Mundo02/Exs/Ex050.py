s = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}° numero: '.format(c)))
    if num % 2 == 0:
        s += num
        cont += 1
print('Quantidade de numeros pares: {}'.format(cont))
print('Soma dos valores pares: {}'.format(s))
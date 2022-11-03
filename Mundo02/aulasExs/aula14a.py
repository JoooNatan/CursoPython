'''c = 1
while c <= 10:
    print(c, end = ' ')
    c += 1'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um numero '))
    r = str(input('Quer continuar?[S/N]')).upper()'''

n = 1
contPar = 0
contImpar = 0

while n != 0:
    n = int(input('Digite um numero '))
    if n != 0:
        if n % 2 == 0:
            contPar += 1
        else:
            contImpar += 1

print('Quantidade de numeros pares: {}\nQuantidade de numeros impares: {}'.format(contPar, contImpar))
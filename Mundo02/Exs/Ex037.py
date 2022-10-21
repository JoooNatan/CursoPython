print('-=' * 10)
print('Conversor de bases')
print('-=' * 10)
num = int(input('Digite um numero intero: '))
print('''Escolha a base para converção
[1] para BINARIO
[2] para OCTAL
[3] para HEXADECIMAL''')
op = int(input('Opção: '))
if op == 1:
    print('{} em binario é igual a : {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} em octal é igual a : {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} em hexadecimal é igual a : {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida!')
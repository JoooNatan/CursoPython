#nome = input('Qual seu nome? ')
#print('Ola {:=^20}'.format(nome))
n1 = int(input('Digite um numero '))
n2 = int(input('Digite outro numero '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s, m, d))
print('Divisão inteira {} e potencia {}'.format(di, e))
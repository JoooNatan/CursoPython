print('\033[32m-=<\033[m\033[33m>=-\033[m' * 5)
print('     Situação militar')
print('\033[32m-=<\033[m\033[33m>=-\033[m' * 5)

idade = int(input('Digite sua idade: '))
if idade < 18:
    print('Você ainda não precisa se alistar')
elif idade == 18:
    print('Você deve se alistar ainda este ano')
else:
    print('Você deveria ter se alistado a {} anos'.format(idade - 18))
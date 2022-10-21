from datetime import date
atual = date.today().year   #pega o ano atual
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = atual - ano
print('O atleta tem {} anos'.format(idade))
print('Categoria: ', end = '')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MESTRE')


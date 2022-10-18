from datetime import date
ano = int(input('Digite um ano para saber se ele é bissexto ou não: '))
if ano == 0:
    ano = date.today().year#Pega o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é \033[32mBISSEXTO\033[m'.format(ano))
else:
    print('O ano {} não é \033[31mBISSEXTO\033[m'.format(ano))

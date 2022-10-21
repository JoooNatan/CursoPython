n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Media: {:.2f}'.format(media))
print('Situação: ', end='')
if media < 5:
    print('\033[31mREPROVADO\033[m')
elif media < 7:
    print('\033[33mRECUPERAÇÃO\033[m')
else:
    print('\033[32mAPROVADO\033[m')

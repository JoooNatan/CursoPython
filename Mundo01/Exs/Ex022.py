nome = str(input('Qual seu nome completo? ')).strip()
print('Analizando o nome..')
print('Nome com todas as letras maiusculas é: {}'.format(nome.upper()))
print('Nome com todas as letras minusculas é: {}'.format(nome.lower()))
print('O nome tem {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('O primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))

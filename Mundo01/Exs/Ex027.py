nome = str(input('Digite seu nome completo ')).strip()
n = nome.split()
print('O primeiro nome é \033[32m{}\033[m'.format(n[0]))
print('O ultimo nome é \033[32m{}\033[m'.format(n[len(n)-1]))

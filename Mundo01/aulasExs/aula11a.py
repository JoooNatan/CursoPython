from cgi import print_arguments


nome = 'Joao'
cores = {'limpa':'\033[m', 'azul':'\033[34m', 'roxo':'\033[35m'}
print('Ola, prazer em te conhecer {}{}{}'.format(cores['azul'], nome, cores['limpa']))
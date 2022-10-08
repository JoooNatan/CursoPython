from random import shuffle

n1 = input('Qual o nome dp primeiro aluno? ')
n2 = input('Qual o nome dp segundo aluno? ')
n3 = input('Qual o nome dp terceiro aluno? ')
n4 = input('Qual o nome dp quarto aluno? ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação sera: ')
print(lista)
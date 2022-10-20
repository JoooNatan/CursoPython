n1 = int(input('Digite o primeiro valor '))
n2 = int(input('Digite o segundo valor '))
if n1 > n2:
    print('O \033[33mprimeiro\033[m valor é o \033[32mmaior!\033[m')
elif n2 > n1:
    print('O \033[33msegundo\033[m valor é o \033[32mmaior!\033[m')
else:
    print('Não existe valor maior, os dois são iguais!')

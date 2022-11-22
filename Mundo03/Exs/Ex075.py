num = (int(input(f'Digite o 1° valor: ')), int(input(f'Digite o 2° valor: ')),
int(input(f'Digite o 3° valor: ')), int(input(f'Digite o 4° valor: ')))

print(num)
if 9 in num:
    print(f'O numero 9 apareceu {num.count(9)} vezes')#num.cout(9) conta quantas vezes o num 9 aparece
else:
    print(f'O numero 9 nao apareceu')

if 3 in num:
    print(f'O valor 3 apareceu na posicao {num.index(3) + 1}')#num.index(3) mostra o index do num 3
else:
    print('O valor 3 nao apareceu nem uma vez')

print('Os valores pares digitados foram ', end = '')

for n in num:
    if n % 2 == 0:
        print(n, end = ' ')